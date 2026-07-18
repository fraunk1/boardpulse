# facts-v2 backfill — paused state (note, 2026-07-17)

Frank asked to note this and return to it later. Two open loose ends:

## 1. Itemized-discipline (facts-v2) re-extraction — PAUSED at 46/115

**Why:** the live DB has 2,040 facts-v1 disciplinary rows where 72% of multi-action
counts aren't visible in their own quote (a model tally, not itemized). facts-v2
re-extracts one row per named respondent so counts become arithmetic. Contract +
gate live in commit `ee3b7ef`; schema already migrated (`respondent` column exists).

**State on disk:** 46 of 115 board-chunks have valid `data/reports/facts/<CHUNK>_facts.json`
(gitignored). **NONE ingested yet** — DB still 100% facts-v1.

**69 chunks still MISSING** (re-check with the disk-reconcile one-liner below, don't trust this list blindly):
```
CT_MD_02 IN_MD_01 IN_MD_02 KS_MD_01 MA_MD_01 MA_MD_02 MD_MD_01 ME_DO_01 ME_MD_01
ME_MD_02 ME_MD_03 ME_MD_04 ME_MD_05 MI_DO_01 MI_MD_01 MI_MD_02 MN_MD_01 MN_MD_02
MO_MD_01 MS_MD_01 MS_MD_02 MT_MD_01 MT_MD_02 NC_MD_01 NC_MD_02 ND_MD_01 NE_MD_01
NH_MD_01 NJ_MD_01 NM_MD_01 NM_MD_02 NV_DO_01 NV_DO_02 NV_MD_01 NV_MD_02 NY_MD_01
NY_MD_02 OH_MD_01 OK_DO_01 OK_MD_01 OK_MD_02 OR_MD_01 OR_MD_02 PA_DO_01 PA_DO_02
PA_MD_01 PA_MD_02 PA_MD_03 RI_MD_01 SC_MD_01 SD_MD_01 TN_DO_01 TN_MD_01 TX_MD_01
UT_MD_01 VA_MD_01 VA_MD_02 VA_MD_03 VA_MD_04 VT_DO_01 VT_MD_01 VT_MD_02 WA_DO_01
WA_MD_01 WA_MD_02 WI_MD_01 WI_MD_02 WV_MD_01 WY_MD_01
```

**Disk-reconcile (authoritative — a chunk is done only if its `_facts.json` parses):**
```bash
cd Projects/boardpulse && ./venv/Scripts/python.exe -c "
import json,pathlib; d=pathlib.Path('data/reports/facts'); ok=[]
[ok.append(p.stem.replace('_facts','')) for p in d.glob('*_facts.json') if (json.loads(p.read_text('utf-8')) or True)]
allp=sorted(x.stem.replace('_facts_prompt','') for x in d.glob('*_facts_prompt.md'))
print('done',len(ok),'missing:',[c for c in allp if c not in ok])"
```

**To resume:** dispatch ONE general-purpose subagent per missing chunk (prompt template:
"read the ENTIRE `<CHUNK>_facts_prompt.md`, follow the facts-v2 contract, write ONLY the
JSON to `<CHUNK>_facts.json`; do NOT dispatch sub-agents; you MUST write the file";
hard rules = quotes exact substrings, itemized discipline w/ respondent, bulk only when
count is verbatim in quote, `schema_version:"facts-v2"`). Keep ~8-10 concurrent, reconcile
against disk after each session usage-limit wall. **Backfill kept hitting the account
usage limit** (reset windows ~every few hrs) — expect to resume across several sittings.

**After all 115 land:** `cli.py facts --ingest` (gated; retry rejects once, skip after 2nd)
→ `cli.py facts --audit` (the count-not-in-quote metric should collapse toward 0 as tally
rows are replaced) → spot-check /trends discipline.

**Gotcha:** a hallucinating subagent once spawned its OWN year-sliced sub-agents that dumped
JSON to chat instead of writing the file (CT_MD_02). Always verify the file exists on disk;
never count an agent's "done" message.

## 2. Dashboard auto-start at login (optional)

The local dashboard (`cli.py serve` → :8099) does NOT survive a reboot and doesn't
auto-start. Offered to register a Windows Task Scheduler job so it launches at login —
Frank said note it for later. To do: `schtasks`/Task Scheduler entry running
`venv\Scripts\python.exe cli.py serve --host 127.0.0.1 --port 8099` (hidden) at logon.
