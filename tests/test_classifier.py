"""Test keyword topic classifier."""
import pytest
from datetime import date, datetime, timezone

from app import database as db
from app.models import Board, Meeting, MeetingDocument, DocumentPage
from app.pipeline.classifier import classify_text, classify_all_documents, TOPIC_PATTERNS
from app.pipeline.context import TOPIC_TAXONOMY


# ---------------------------------------------------------------------------
# classify_text — unit tests
# ---------------------------------------------------------------------------

def test_classify_empty_text():
    assert classify_text("") == []


def test_classify_short_text():
    assert classify_text("Board met.") == []


def test_classify_no_matches():
    assert classify_text("The weather today is sunny and warm. " * 10) == []


def test_classify_discipline():
    text = (
        "The board reviewed a consent order for Dr. Smith who was placed on probation. "
        "A second disciplinary action involved license suspension for misconduct."
    )
    result = classify_text(text)
    assert "Discipline" in result


def test_classify_telehealth():
    text = (
        "Discussion of telehealth prescribing authority. The committee reviewed "
        "telemedicine regulations for virtual care consultations across state lines."
    )
    result = classify_text(text)
    assert "Telehealth" in result


def test_classify_ai_technology():
    text = (
        "The board discussed artificial intelligence use in clinical diagnosis. "
        "A presentation on machine learning algorithms in medical imaging was given."
    )
    result = classify_text(text)
    assert "AI & Technology" in result


def test_classify_licensing():
    text = (
        "License renewal applications were reviewed. The board processed "
        "endorsement requests and discussed reciprocity agreements."
    )
    result = classify_text(text)
    assert "Licensing" in result


def test_classify_rulemaking():
    text = (
        "The proposed rule amendments to administrative code section 22 were discussed. "
        "A rulemaking hearing was scheduled for public comment on the regulation change."
    )
    result = classify_text(text)
    assert "Rulemaking" in result


def test_classify_multiple_topics():
    text = (
        "The board issued a consent order after receiving a complaint about opioid overprescribing. "
        "Probation was imposed and prescribing of controlled substances was restricted. "
        "Patient safety protocols and adverse event reporting were also reviewed."
    )
    result = classify_text(text)
    assert "Discipline" in result
    assert "Opioids & Prescribing" in result
    assert "Patient Safety" in result


def test_classify_min_matches_threshold():
    text = "The board reviewed one license application and adjourned. " * 3
    assert "Licensing" in classify_text(text, min_matches=1)
    single = "The board discussed a single licensing matter."
    assert classify_text(single, min_matches=2) == [] or "Licensing" not in classify_text(single, min_matches=2)


def test_classify_results_sorted():
    text = (
        "Telehealth prescribing and telemedicine rules. "
        "Disciplinary consent orders and license suspensions. "
        "AI and artificial intelligence in healthcare. "
    )
    result = classify_text(text, min_matches=1)
    assert result == sorted(result)


def test_all_16_topics_matchable():
    """Each of the 16 topic patterns can be triggered independently."""
    test_snippets = {
        "Licensing": "license renewal applications endorsement processing",
        "Discipline": "A complaint was filed and the consent order required probation for misconduct",
        "Telehealth": "telehealth telemedicine and virtual care prescribing standards",
        "AI & Technology": "artificial intelligence machine learning algorithm",
        "Rulemaking": "rulemaking proposed rule administrative code amendment",
        "Budget & Finance": "budget financial report fiscal year audit expenditure",
        "Board Operations": "board meeting executive director quorum strategic plan",
        "Continuing Education": "continuing medical education CME credit requirements",
        "Scope of Practice": "scope of practice physician assistant PA supervision",
        "Opioids & Prescribing": "opioid controlled substance prescribing pain management",
        "Public Health": "public health emergency pandemic vaccination immunization response",
        "Patient Safety": "patient safety standard of care adverse event quality",
        "Legal": "litigation attorney general legislative update house bill SB 100",
        "Workforce": "physician workforce shortage rural health GME residency",
        "Ethics": "ethics conflict of interest boundary violation professional conduct",
        "Interstate Compact": "interstate compact IMLC compact commission multi-state",
    }
    for topic_name, snippet in test_snippets.items():
        result = classify_text(snippet, min_matches=1)
        assert topic_name in result, f"Topic '{topic_name}' not matched by: {snippet}"


def test_taxonomy_matches_classifier():
    """TOPIC_TAXONOMY in context.py stays in sync with classifier patterns."""
    classifier_topics = sorted([name for name, _ in TOPIC_PATTERNS])
    taxonomy_topics = sorted(TOPIC_TAXONOMY)
    assert classifier_topics == taxonomy_topics, (
        f"Mismatch:\n  Classifier: {classifier_topics}\n  Taxonomy:   {taxonomy_topics}"
    )


# ---------------------------------------------------------------------------
# classify_all_documents — integration tests
# ---------------------------------------------------------------------------

async def _seed_docs_for_classification(seed_board):
    """Helper: create a board with 3 documents, varying text."""
    board = await seed_board()
    async with db.async_session() as session:
        m = Meeting(board_id=board.id, meeting_date=date(2026, 3, 15), title="March")
        session.add(m)
        await session.commit()
        await session.refresh(m)

        d1 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="a.pdf", file_path="/tmp/a.pdf",
            content_text=(
                "The board received a complaint against a physician and issued "
                "a consent order for prescribing opioid controlled substances "
                "without proper monitoring. Probation was imposed."
            ),
        )
        d2 = MeetingDocument(
            meeting_id=m.id, doc_type="agenda",
            filename="b.pdf", file_path="/tmp/b.pdf",
            content_text=(
                "Telehealth prescribing regulations and telemedicine "
                "virtual care standards were discussed at length."
            ),
        )
        d3 = MeetingDocument(
            meeting_id=m.id, doc_type="minutes",
            filename="c.pdf", file_path="/tmp/c.pdf",
            content_text=None,
        )
        session.add_all([d1, d2, d3])
        await session.commit()
    return board, m


async def test_classify_all_documents(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    result = await classify_all_documents()
    assert result["documents_classified"] >= 2
    assert result["meetings_rolled_up"] >= 1

    async with db.async_session() as session:
        m = await session.get(Meeting, meeting.id)
        assert m.topics is not None
        assert len(m.topics) > 0
        assert "Discipline" in m.topics


async def test_classify_skip_existing(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    r1 = await classify_all_documents()
    count1 = r1["documents_classified"]

    r2 = await classify_all_documents(force=False)
    assert r2["documents_classified"] == 0


async def test_classify_force_retag(seed_board):
    board, meeting = await _seed_docs_for_classification(seed_board)
    await classify_all_documents()
    r2 = await classify_all_documents(force=True)
    assert r2["documents_classified"] >= 2


async def test_classify_rollup_dedup(seed_board):
    """Two docs on same meeting with overlapping topics — meeting.topics is deduplicated."""
    board, meeting = await _seed_docs_for_classification(seed_board)
    await classify_all_documents()

    async with db.async_session() as session:
        m = await session.get(Meeting, meeting.id)
        assert len(m.topics) == len(set(m.topics))
        assert m.topics == sorted(m.topics)
