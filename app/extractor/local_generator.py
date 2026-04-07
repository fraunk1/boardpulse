"""Local LLM generation for boardpulse summaries.

Calls a local LLM (Ollama by default, LM Studio fallback) to process prompt files
written by the prepare_* functions, producing output files for the ingest_* functions.

For Ollama endpoints, uses the native /api/generate endpoint so we can pass the
`think` parameter — reasoning models like gemma4:e2b and deepseek-r1 would otherwise
route all output to a separate thinking channel, returning empty `content` on the
OpenAI-compat /v1/chat/completions endpoint. For LM Studio, falls back to the
OpenAI-compatible endpoint.

Configure via environment variables:
    BOARDPULSE_LLM_URL    — base URL (default: http://localhost:11434/v1)
    BOARDPULSE_LLM_MODEL  — model name (default: gemma4:e2b)
    BOARDPULSE_LLM_THINK  — "1"/"true" to enable reasoning channel on supported
                            models (default: disabled — faster, direct answers)
"""
import os
from pathlib import Path

import httpx


DEFAULT_URL = os.environ.get("BOARDPULSE_LLM_URL", "http://localhost:11434/v1")
DEFAULT_MODEL = os.environ.get("BOARDPULSE_LLM_MODEL", "gemma4:e2b")
DEFAULT_THINK = os.environ.get("BOARDPULSE_LLM_THINK", "").lower() in ("1", "true", "yes")
FALLBACK_URLS = ["http://localhost:11434/v1", "http://localhost:1234/v1"]


def _detect_endpoint() -> str:
    """Find the first reachable local LLM endpoint."""
    candidates = [DEFAULT_URL] + [u for u in FALLBACK_URLS if u != DEFAULT_URL]
    for url in candidates:
        try:
            r = httpx.get(f"{url}/models", timeout=2.0)
            if r.status_code == 200:
                return url
        except Exception:
            continue
    raise RuntimeError(
        f"No local LLM reachable. Tried: {candidates}. "
        f"Start Ollama (`ollama serve`) or LM Studio."
    )


def _is_ollama(base_url: str) -> bool:
    """Heuristic: Ollama defaults to port 11434, LM Studio to 1234."""
    return "11434" in base_url


def generate(prompt: str, max_tokens: int = 800, temperature: float = 0.3,
             model: str | None = None, url: str | None = None,
             think: bool | None = None) -> str:
    """Call the local LLM with a single prompt and return the text response.

    For Ollama endpoints, uses the native /api/generate endpoint with the `think`
    flag so reasoning models (gemma4, deepseek-r1) return actual content instead
    of routing everything to a silent thinking channel. For non-Ollama endpoints,
    uses OpenAI-compatible /chat/completions.

    Args:
        prompt: The user prompt.
        max_tokens: Max tokens in the response.
        temperature: Sampling temperature.
        model: Override model name (default: BOARDPULSE_LLM_MODEL).
        url: Override endpoint URL (default: auto-detect).
        think: For reasoning models, whether to generate chain-of-thought
            reasoning before the answer. None uses BOARDPULSE_LLM_THINK env var
            (default False). Ignored on non-Ollama endpoints.
    """
    base_url = url or _detect_endpoint()
    model_name = model or DEFAULT_MODEL
    use_think = DEFAULT_THINK if think is None else think

    if _is_ollama(base_url):
        # Strip /v1 suffix — Ollama's native API is at the root path.
        ollama_base = base_url.rsplit("/v1", 1)[0].rstrip("/")
        response = httpx.post(
            f"{ollama_base}/api/generate",
            json={
                "model": model_name,
                "prompt": prompt,
                "stream": False,
                "think": use_think,
                "options": {
                    "temperature": temperature,
                    "num_predict": max_tokens,
                },
            },
            timeout=600.0,  # generation can be slow on first call
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "").strip()

    # LM Studio / other OpenAI-compat endpoint — no think parameter support.
    response = httpx.post(
        f"{base_url}/chat/completions",
        json={
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
        },
        timeout=600.0,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"].strip()


def process_prompt_files(
    prompt_dir: Path,
    pattern: str = "*.prompt.md",
    max_tokens: int = 800,
    temperature: float = 0.3,
    skip_existing: bool = True,
    model: str | None = None,
    think: bool | None = None,
) -> tuple[int, int, int]:
    """Process all prompt files in a directory, writing output files alongside them.

    For each `{name}.prompt.md`, writes `{name}.md` with the LLM response.

    Args:
        prompt_dir: Directory containing prompt files
        pattern: Glob pattern for prompt files
        max_tokens: Max tokens per response
        temperature: Sampling temperature
        skip_existing: Skip prompts whose output file already exists
        model: Override model name (default: BOARDPULSE_LLM_MODEL)
        think: Pass-through to generate() — reasoning channel control for Ollama

    Returns:
        (generated, skipped, errors) counts
    """
    base_url = _detect_endpoint()
    model_name = model or DEFAULT_MODEL

    think_suffix = ""
    if _is_ollama(base_url):
        effective_think = DEFAULT_THINK if think is None else think
        think_suffix = f" | think: {effective_think}"
    print(f"Local LLM: {base_url} | model: {model_name}{think_suffix}")

    prompt_files = sorted(prompt_dir.glob(pattern))
    if not prompt_files:
        print(f"No prompt files found in {prompt_dir} matching {pattern}")
        return 0, 0, 0

    generated = 0
    skipped = 0
    errors = 0

    for i, prompt_path in enumerate(prompt_files, 1):
        # Output filename: drop the .prompt suffix
        # MO_MD_brief_quarter.prompt.md → MO_MD_brief_quarter.md
        # MO_MD_649.prompt.md → MO_MD_649.md
        output_name = prompt_path.name.replace(".prompt.md", ".md")
        output_path = prompt_path.parent / output_name

        if skip_existing and output_path.exists() and output_path.stat().st_size > 0:
            skipped += 1
            continue

        prompt_text = prompt_path.read_text(encoding="utf-8")

        try:
            result = generate(
                prompt_text,
                max_tokens=max_tokens,
                temperature=temperature,
                model=model_name,
                url=base_url,
                think=think,
            )
            output_path.write_text(result, encoding="utf-8")
            generated += 1
            print(f"  [{i}/{len(prompt_files)}] {output_name} → {len(result)} chars")
        except Exception as e:
            errors += 1
            print(f"  [{i}/{len(prompt_files)}] {output_name} → ERROR: {e}")

    print(f"\nGenerated {generated}, skipped {skipped}, errors {errors}.")
    return generated, skipped, errors
