"""SQLAlchemy models for boardpulse."""
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import (
    CheckConstraint, Integer, String, Text, Date, DateTime, ForeignKey, JSON,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.quality.taxonomy import (
    _check, CONFIDENCE, DISCIPLINE_CATEGORIES, INSTRUMENTS, INVOLVEMENTS,
    STAGES, TOPICS,
)


class Base(DeclarativeBase):
    pass


class Board(Base):
    __tablename__ = "boards"

    id: Mapped[int] = mapped_column(primary_key=True)
    state: Mapped[str] = mapped_column(String(2))
    code: Mapped[str] = mapped_column(String(10), unique=True)
    name: Mapped[str] = mapped_column(String(200))
    board_type: Mapped[str] = mapped_column(String(10))  # "MD", "DO", "combined"
    homepage: Mapped[str] = mapped_column(Text)
    minutes_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    phone: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    email: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    discovery_status: Mapped[str] = mapped_column(String(20), default="pending")
    last_scraped_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    # 12-month AI rollup for the board (shown on the board page; meeting
    # pages carry their OWN summaries in Meeting.summary)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summarized_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    meetings: Mapped[list["Meeting"]] = relationship(back_populates="board", cascade="all, delete-orphan")


class Meeting(Base):
    __tablename__ = "meetings"

    id: Mapped[int] = mapped_column(primary_key=True)
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"), index=True)
    meeting_date: Mapped[date] = mapped_column(Date, index=True)
    title: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    meeting_type: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    source_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    screenshot_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    # THIS meeting's own AI summary + topics (per-meeting since the
    # per-meeting-summaries change; formerly held a board-level copy)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    topics: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    summarized_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    # set when a facts file covering this meeting is ingested (even with zero
    # facts found) — the delta driver for monthly fact extraction
    facts_extracted_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    scraped_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    board: Mapped["Board"] = relationship(back_populates="meetings")
    documents: Mapped[list["MeetingDocument"]] = relationship(back_populates="meeting", cascade="all, delete-orphan")


class MeetingDocument(Base):
    __tablename__ = "meeting_documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), index=True)
    doc_type: Mapped[str] = mapped_column(String(20))  # "minutes", "agenda", "notice", "attachment"
    filename: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(Text)
    source_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    content_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    scraped_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    meeting: Mapped["Meeting"] = relationship(back_populates="documents")


# ---------------------------------------------------------------------------
# Structured facts — four typed tables + provenance. The CHECK constraints
# are deliberate: the schema itself rejects enum values the taxonomy doesn't
# allow, so a weaker extraction model cannot quietly widen the vocabulary.
# ---------------------------------------------------------------------------

class ExtractionRun(Base):
    """Provenance for one ingested facts file."""
    __tablename__ = "extraction_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"), index=True)
    model: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    prompt_version: Mapped[str] = mapped_column(String(20))
    source_file: Mapped[str] = mapped_column(Text)
    window_start: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    window_end: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    meetings_covered: Mapped[int] = mapped_column(Integer, default=0)
    facts_inserted: Mapped[int] = mapped_column(Integer, default=0)
    status: Mapped[str] = mapped_column(
        String(10), CheckConstraint("status IN ('ingested', 'failed')"))
    error: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc))


class PolicyAction(Base):
    """Fact class 1: policy positions & rulemaking activity."""
    __tablename__ = "policy_actions"
    __table_args__ = (
        UniqueConstraint("meeting_id", "fact_hash"),
        CheckConstraint(_check("instrument", INSTRUMENTS)),
        CheckConstraint(_check("stage", STAGES)),
        CheckConstraint(_check("topic", TOPICS)),
        CheckConstraint(_check("confidence", CONFIDENCE)),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("extraction_runs.id"))
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), index=True)
    document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("meeting_documents.id"), nullable=True)
    instrument: Mapped[str] = mapped_column(String(20))
    stage: Mapped[str] = mapped_column(String(20))
    topic: Mapped[str] = mapped_column(String(30))
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    rule_reference: Mapped[Optional[str]] = mapped_column(String(120), nullable=True)
    action_date: Mapped[date] = mapped_column(Date)
    quote: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confidence: Mapped[str] = mapped_column(String(10))
    fact_hash: Mapped[str] = mapped_column(String(64))


class LegislationMention(Base):
    """Fact class 2: bills the board discussed."""
    __tablename__ = "legislation_mentions"
    __table_args__ = (
        UniqueConstraint("meeting_id", "fact_hash"),
        CheckConstraint(_check("involvement", INVOLVEMENTS)),
        CheckConstraint(_check("confidence", CONFIDENCE)),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("extraction_runs.id"))
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), index=True)
    document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("meeting_documents.id"), nullable=True)
    bill_number: Mapped[str] = mapped_column(String(30))
    bill_state: Mapped[str] = mapped_column(String(2))
    subject: Mapped[str] = mapped_column(Text)
    topic: Mapped[Optional[str]] = mapped_column(
        String(30), CheckConstraint(_check("topic", TOPICS)), nullable=True)
    involvement: Mapped[str] = mapped_column(String(20))
    status_note: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    quote: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confidence: Mapped[str] = mapped_column(String(10))
    fact_hash: Mapped[str] = mapped_column(String(64))


class DisciplinaryAction(Base):
    """Fact class 3: itemized disciplinary actions (facts-v2).

    One row per action: an ITEMIZED row carries the respondent (practitioner
    name or case number as written) with action_count=1, so totals are
    arithmetic over rows, not model-made tallies. A BULK row (respondent
    NULL, action_count>=2) is allowed only when the document itself states
    the total — the gate requires the number to be visible in the quote.
    Legacy facts-v1 tally rows (respondent NULL, count unverified) remain
    until the re-extraction backfill replaces them.
    """
    __tablename__ = "disciplinary_actions"
    __table_args__ = (
        CheckConstraint(_check("category", DISCIPLINE_CATEGORIES)),
        CheckConstraint("action_count >= 0"),
        CheckConstraint(_check("confidence", CONFIDENCE)),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("extraction_runs.id"))
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), index=True)
    document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("meeting_documents.id"), nullable=True)
    category: Mapped[str] = mapped_column(String(20))
    respondent: Mapped[Optional[str]] = mapped_column(
        String(200), nullable=True)
    action_count: Mapped[int] = mapped_column(Integer)
    quote: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    confidence: Mapped[str] = mapped_column(String(10))


class EmergingTopic(Base):
    """Fact class 4: board-scoped first mentions of new subjects.

    UNIQUE(board_id, topic_slug): ingest upserts and keeps the EARLIEST
    first_mentioned_on, so re-extraction can only sharpen the timeline.
    """
    __tablename__ = "emerging_topics"
    __table_args__ = (
        UniqueConstraint("board_id", "topic_slug"),
        CheckConstraint(_check("confidence", CONFIDENCE)),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("extraction_runs.id"))
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"), index=True)
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"))
    document_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("meeting_documents.id"), nullable=True)
    topic_slug: Mapped[str] = mapped_column(String(60))
    subject: Mapped[str] = mapped_column(Text)
    first_mentioned_on: Mapped[date] = mapped_column(Date, index=True)
    quote: Mapped[str] = mapped_column(Text)  # required — fabrication anchor
    confidence: Mapped[str] = mapped_column(String(10))


# ---------------------------------------------------------------------------
# Refresh history — deltas become queryable instead of living in log files.
# ---------------------------------------------------------------------------

class RefreshRun(Base):
    __tablename__ = "refresh_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    board_filter: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    boards_changed: Mapped[int] = mapped_column(Integer, default=0)
    boards_regressed: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    docs_before: Mapped[int] = mapped_column(Integer, default=0)
    docs_after: Mapped[int] = mapped_column(Integer, default=0)
    log_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    exit_code: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)


class BoardSnapshot(Base):
    __tablename__ = "board_snapshots"
    __table_args__ = (UniqueConstraint("run_id", "board_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("refresh_runs.id"))
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"), index=True)
    mtgs: Mapped[int] = mapped_column(Integer, default=0)
    docs: Mapped[int] = mapped_column(Integer, default=0)
    docs_text: Mapped[int] = mapped_column(Integer, default=0)
    mtgs_summarized: Mapped[int] = mapped_column(Integer, default=0)
    mtgs_facts: Mapped[int] = mapped_column(Integer, default=0)


class WatchlistTerm(Base):
    """A standing full-text query Frank watches (AI, telehealth, ...)."""
    __tablename__ = "watchlist_terms"

    id: Mapped[int] = mapped_column(primary_key=True)
    term: Mapped[str] = mapped_column(String(120), unique=True)
    label: Mapped[str] = mapped_column(String(80))
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc))
    acknowledged_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True)
