"""Classify documents into topic categories using keyword matching or local LLM.

Two backends:
  1. Regex classifier (default) — fast keyword matching, no AI, good for 80%+ of content
  2. LLM classifier (--llm flag) — local Ollama call for higher accuracy on ambiguous text

Topic taxonomy is tailored to state medical board meeting minutes.
"""
import json
import re
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import select, func

import app.database as db
from app.models import Meeting, MeetingDocument, DocumentPage, Board
from app.config import REPORTS_DIR

# ─── Topic Taxonomy ──────────────────────────────────────────────────────────
# Each topic has a canonical name and keyword patterns (case-insensitive).
# Patterns are compiled regexes for speed over 1,600+ documents.

TOPIC_PATTERNS: list[tuple[str, re.Pattern]] = [
    ("Licensing", re.compile(
        r"\b(licens|renewal|initial license|license application|endorse(?:ment)?|"
        r"reciproc|compact license|IMLCC?|interstate medical licens)\b", re.I)),
    ("Discipline", re.compile(
        r"\b(disciplin|complaint|revoc|suspend|probation|consent (?:order|agreement)|"
        r"surrender|reprimand|stipulat|malpractice|misconduct|impair(?:ed|ment)|"
        r"diversion|monitoring|enforcement action|final order)\b", re.I)),
    ("Telehealth", re.compile(
        r"\b(telehealth|telemedicine|telemed|remote (?:patient|practice|prescrib)|"
        r"virtual (?:care|visit|consult))\b", re.I)),
    ("AI & Technology", re.compile(
        r"\b(artificial intelligence|(?<!\w)AI(?!\w)|machine learning|algorithm|"
        r"chatbot|large language model|LLM|deep ?learn|neural net|"
        r"electronic (?:health|medical) record|EHR|EMR|health ?IT|PDMP|"
        r"prescription drug monitoring)\b", re.I)),
    ("Rulemaking", re.compile(
        r"\b(rulemaking|rule(?:s)? (?:hearing|change|amendment|proposal|adopt)|"
        r"proposed rule|administrative code|regulation (?:change|update|proposal)|"
        r"public comment|notice of intent|promulgat)\b", re.I)),
    ("Budget & Finance", re.compile(
        r"\b(budget|financial (?:report|statement|review)|fiscal year|revenue|"
        r"expenditure|audit|fee (?:schedule|increase|reduction)|appropriation|"
        r"contract(?:s)? (?:award|renew)|procurement)\b", re.I)),
    ("Board Operations", re.compile(
        r"\b(board (?:meeting|election|member|composition|governance|retreat)|"
        r"executive session|executive director|quorum|bylaws|strategic plan|"
        r"committee (?:report|meeting)|annual report|staff(?:ing)? (?:report|update))\b", re.I)),
    ("Continuing Education", re.compile(
        r"\b(continuing (?:medical )?education|CME|CE (?:requirement|credit|hour)|"
        r"maintenance of (?:licensure|certification)|MOL|MOC)\b", re.I)),
    ("Scope of Practice", re.compile(
        r"\b(scope of practice|physician assistant|PA (?:supervision|practice)|"
        r"nurse practitioner|NP (?:supervision|independent)|"
        r"collaborative (?:agreement|practice)|supervisory|APRN|"
        r"advanced practice)\b", re.I)),
    ("Opioids & Prescribing", re.compile(
        r"\b(opioid|controlled substance|prescrib(?:ing|er)|"
        r"pain (?:management|clinic)|(?:drug|substance) (?:abuse|use)|"
        r"addiction|naloxone|buprenorphine|MAT|MATE Act|"
        r"overprescri|pill mill)\b", re.I)),
    ("Public Health", re.compile(
        r"\b(public health|pandemic|COVID|vaccination|immuniz|"
        r"infectious disease|emergency (?:order|declaration)|"
        r"mental health|suicide|health equity|dispari|"
        r"maternal (?:health|mortality)|preventive)\b", re.I)),
    ("Patient Safety", re.compile(
        r"\b(patient safety|standard of care|medical error|adverse event|"
        r"sentinel event|quality (?:improvement|assurance)|"
        r"peer review|hospital privileging|credentialing)\b", re.I)),
    ("Legal", re.compile(
        r"\b(litigation|lawsuit|court (?:order|ruling|decision)|"
        r"attorney general|legislative (?:update|session|bill)|"
        r"statutory (?:change|authority)|house bill|senate bill|"
        r"HB \d|SB \d|legal (?:counsel|report|update))\b", re.I)),
    ("Workforce", re.compile(
        r"\b(physician (?:workforce|shortage|supply|distribution)|"
        r"recruitment|retention|rural (?:health|access)|"
        r"underserved|GME|graduate medical education|residency|"
        r"IMG|international medical graduate|foreign medical)\b", re.I)),
    ("Ethics", re.compile(
        r"\b(ethic(?:s|al)|conflict of interest|sexual (?:misconduct|boundary)|"
        r"boundary violation|professional (?:conduct|boundary)|"
        r"informed consent|fiduciary)\b", re.I)),
    ("Interstate Compact", re.compile(
        r"\b(interstate (?:compact|medical licensure)|IMLC|IMLCC|"
        r"compact (?:commission|license|application|member)|"
        r"multi-?state|expedited licens)\b", re.I)),
]


TOPIC_NAMES: list[str] = [name for name, _ in TOPIC_PATTERNS]


def classify_text(text: str, min_matches: int = 2) -> list[str]:
    """Classify a document's text into topic categories using regex patterns.

    Args:
        text: Document content text.
        min_matches: Minimum keyword hits to assign a topic (reduces false positives).

    Returns:
        Sorted list of topic names.
    """
    if not text or len(text) < 50:
        return []

    topics = []
    for topic_name, pattern in TOPIC_PATTERNS:
        matches = pattern.findall(text)
        if len(matches) >= min_matches:
            topics.append(topic_name)

    return sorted(topics)


def _llm_classify_prompt(text: str, max_chars: int = 5000) -> str:
    """Build a topic-classification prompt for a local LLM."""
    topics_list = "\n".join(f"- {t}" for t in TOPIC_NAMES)
    snippet = text[:max_chars]
    return (
        "You are classifying a page from a state medical board meeting document into topic categories.\n\n"
        f"TOPIC CATEGORIES (pick 0 to 4 that apply, exact spelling):\n{topics_list}\n\n"
        "Rules:\n"
        "- Only pick topics that are clearly discussed on this page.\n"
        "- It is OK to pick zero topics if the page is administrative boilerplate or table-of-contents only.\n"
        "- Pick at most 4 — focus on the most relevant.\n"
        "- Output ONLY a comma-separated list of topic names. No prose, no explanation, no markdown.\n\n"
        f"PAGE TEXT:\n{snippet}\n\n"
        "CLASSIFICATION:"
    )


def classify_text_llm(text: str, model: str | None = None) -> list[str]:
    """Classify text into topics using a local LLM (Ollama by default).

    Returns canonical topic names from TOPIC_PATTERNS — names that don't match
    the canonical list are dropped, so output is always trustworthy.

    Args:
        text: Document or page text content.
        model: Override LLM model name (default: BOARDPULSE_LLM_MODEL).

    Returns:
        Sorted list of topic names from the canonical taxonomy.
    """
    if not text or len(text) < 50:
        return []

    from app.extractor.local_generator import generate

    prompt = _llm_classify_prompt(text)
    try:
        response = generate(
            prompt,
            max_tokens=80,
            temperature=0.1,
            model=model,
            think=False,
        )
    except Exception as e:
        print(f"    LLM classification error: {e}")
        return []

    # Parse comma-separated topics; validate against canonical taxonomy.
    canonical = {name.lower(): name for name in TOPIC_NAMES}
    raw_parts = [t.strip().strip("-").strip("*").strip() for t in response.split(",")]
    valid: set[str] = set()
    for part in raw_parts:
        if not part:
            continue
        # Some models prefix with bullets or numbers — strip them.
        cleaned = part.lstrip("0123456789. )").strip()
        if cleaned.lower() in canonical:
            valid.add(canonical[cleaned.lower()])
    return sorted(valid)


async def classify_all_documents(
    force: bool = False,
    min_matches: int = 2,
    backend: str = "regex",
) -> dict:
    """Classify all documents with extracted text and store topics.

    Args:
        force: Re-classify even if topics already exist.
        min_matches: Minimum keyword hits per topic (regex backend only).
        backend: 'regex' (default, fast) or 'llm' (local Ollama, more accurate).

    Returns:
        Summary dict with counts.
    """
    if db.engine is None:
        await db.init_db()

    async with db.async_session() as session:
        query = select(MeetingDocument.id, MeetingDocument.content_text, MeetingDocument.topics)
        if not force:
            query = query.where(
                (MeetingDocument.topics.is_(None)) | (MeetingDocument.topics == "[]")
            )
        query = query.where(MeetingDocument.content_text.isnot(None))
        docs = (await session.execute(query)).all()

    print(f"  Classifying {len(docs)} documents (backend={backend})...")

    classified = 0
    topics_json: dict[str, list[str]] = {}
    meetings_to_rollup: set[int] = set()

    for doc_id, content_text, existing_topics in docs:
        if backend == "llm":
            topics = classify_text_llm(content_text)
        else:
            topics = classify_text(content_text, min_matches=min_matches)
        if not topics:
            continue

        topics_json[str(doc_id)] = topics

        async with db.async_session() as session:
            doc = await session.get(MeetingDocument, doc_id)
            doc.topics = topics
            meetings_to_rollup.add(doc.meeting_id)
            await session.commit()
        classified += 1

    # Rollup to meetings
    meetings_rolled = 0
    for meeting_id in meetings_to_rollup:
        async with db.async_session() as session:
            docs = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == meeting_id)
                .where(MeetingDocument.topics.isnot(None))
            )).scalars().all()

            all_topics: set[str] = set()
            for doc in docs:
                tags = doc.topics if isinstance(doc.topics, list) else json.loads(doc.topics or "[]")
                all_topics.update(tags)

            meeting = await session.get(Meeting, meeting_id)
            if meeting and all_topics:
                meeting.topics = sorted(all_topics)
                await session.commit()
                meetings_rolled += 1

    # Write JSON for reference
    output_path = REPORTS_DIR / "document_topics.json"
    output_path.write_text(json.dumps(topics_json, indent=2), encoding="utf-8")

    print(f"  Classified {classified} documents into topics")
    print(f"  Rolled up topics to {meetings_rolled} meetings")
    print(f"  Topics JSON saved to {output_path}")

    # Print topic distribution
    all_topic_counts: dict[str, int] = {}
    for topics in topics_json.values():
        for t in topics:
            all_topic_counts[t] = all_topic_counts.get(t, 0) + 1

    print("\n  Topic Distribution:")
    for topic, count in sorted(all_topic_counts.items(), key=lambda x: -x[1]):
        print(f"    {topic:<25s} {count:>5d} documents")

    return {
        "documents_classified": classified,
        "meetings_rolled_up": meetings_rolled,
        "topic_distribution": all_topic_counts,
    }


async def classify_pages_for_document(
    document_id: int,
    min_matches: int = 1,
    backend: str = "regex",
) -> int:
    """Extract text per page via PyMuPDF and classify each page.

    Args:
        document_id: ID of the MeetingDocument.
        min_matches: Min keyword hits per topic (regex backend only).
        backend: 'regex' (default) or 'llm' (Ollama).

    Returns:
        Number of pages tagged.
    """
    import fitz
    from app.config import PROJECT_ROOT

    if db.engine is None:
        await db.init_db()

    async with db.async_session() as session:
        doc = await session.get(MeetingDocument, document_id)
        if not doc:
            return 0

        pages = (await session.execute(
            select(DocumentPage)
            .where(DocumentPage.document_id == document_id)
            .where(DocumentPage.topics.is_(None))
            .order_by(DocumentPage.page_number)
        )).scalars().all()

        if not pages:
            return 0

    file_path = Path(doc.file_path)
    if not file_path.is_absolute():
        file_path = PROJECT_ROOT / file_path
    if not file_path.exists() or file_path.suffix.lower() != ".pdf":
        return 0

    try:
        pdf = fitz.open(str(file_path))
    except Exception:
        return 0

    now = datetime.now(timezone.utc)
    tagged = 0

    for page_obj in pages:
        page_idx = page_obj.page_number - 1
        if page_idx >= len(pdf):
            continue

        page_text = pdf[page_idx].get_text()
        if backend == "llm":
            topics = classify_text_llm(page_text)
        else:
            topics = classify_text(page_text, min_matches=min_matches)

        if topics:
            async with db.async_session() as session:
                dp = await session.get(DocumentPage, page_obj.id)
                dp.topics = topics
                dp.tagged_at = now
                await session.commit()
            tagged += 1

    pdf.close()
    return tagged


async def classify_all_pages(
    force: bool = False,
    min_matches: int = 1,
    backend: str = "regex",
) -> dict:
    """Classify all rendered pages by extracting text per page from PDFs.

    Args:
        force: Re-classify even if topics already exist.
        min_matches: Minimum keyword hits per topic (regex backend only).
        backend: 'regex' (default, fast) or 'llm' (local Ollama, slower but more accurate).

    Returns:
        Summary dict.
    """
    if db.engine is None:
        await db.init_db()

    # Get documents that have rendered pages
    async with db.async_session() as session:
        query = (
            select(func.distinct(DocumentPage.document_id))
        )
        if not force:
            # Only documents where at least one page has no topics
            from sqlalchemy import exists
            subq = (
                select(DocumentPage.id)
                .where(DocumentPage.document_id == DocumentPage.document_id)
                .where(DocumentPage.topics.is_(None))
            )
            query = select(func.distinct(DocumentPage.document_id)).where(
                DocumentPage.topics.is_(None)
            )
        doc_ids = [row[0] for row in (await session.execute(query)).all()]

    print(f"  Tagging pages for {len(doc_ids)} documents (backend={backend})...")

    total_tagged = 0
    progress_step = 10 if backend == "llm" else 100
    for i, doc_id in enumerate(doc_ids, 1):
        tagged = await classify_pages_for_document(
            doc_id, min_matches=min_matches, backend=backend,
        )
        total_tagged += tagged
        if i % progress_step == 0:
            print(f"    ... processed {i}/{len(doc_ids)} documents ({total_tagged} pages tagged)")

    # Rollup page topics to documents and meetings
    print(f"  Rolling up page topics to documents...")
    docs_rolled = 0
    meetings_to_rollup: set[int] = set()

    for doc_id in doc_ids:
        async with db.async_session() as session:
            pages = (await session.execute(
                select(DocumentPage)
                .where(DocumentPage.document_id == doc_id)
                .where(DocumentPage.topics.isnot(None))
            )).scalars().all()

            if not pages:
                continue

            all_topics: set[str] = set()
            for p in pages:
                tags = p.topics if isinstance(p.topics, list) else json.loads(p.topics or "[]")
                all_topics.update(tags)

            doc = await session.get(MeetingDocument, doc_id)
            if doc and all_topics:
                # Merge with existing document topics
                existing = set(doc.topics or [])
                merged = sorted(existing | all_topics)
                doc.topics = merged
                meetings_to_rollup.add(doc.meeting_id)
                await session.commit()
                docs_rolled += 1

    print(f"  Rolling up to meetings...")
    meetings_rolled = 0
    for meeting_id in meetings_to_rollup:
        async with db.async_session() as session:
            docs = (await session.execute(
                select(MeetingDocument)
                .where(MeetingDocument.meeting_id == meeting_id)
                .where(MeetingDocument.topics.isnot(None))
            )).scalars().all()

            all_topics: set[str] = set()
            for d in docs:
                tags = d.topics if isinstance(d.topics, list) else json.loads(d.topics or "[]")
                all_topics.update(tags)

            meeting = await session.get(Meeting, meeting_id)
            if meeting and all_topics:
                meeting.topics = sorted(all_topics)
                await session.commit()
                meetings_rolled += 1

    print(f"\n  Results:")
    print(f"    Pages tagged:    {total_tagged}")
    print(f"    Documents rolled up: {docs_rolled}")
    print(f"    Meetings rolled up:  {meetings_rolled}")

    return {
        "pages_tagged": total_tagged,
        "documents_rolled_up": docs_rolled,
        "meetings_rolled_up": meetings_rolled,
    }
