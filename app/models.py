"""SQLAlchemy models for boardpulse."""
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import String, Text, Date, DateTime, Float, Integer, ForeignKey, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


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

    meetings: Mapped[list["Meeting"]] = relationship(back_populates="board", cascade="all, delete-orphan")


class Meeting(Base):
    __tablename__ = "meetings"

    id: Mapped[int] = mapped_column(primary_key=True)
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))
    meeting_date: Mapped[date] = mapped_column(Date)
    title: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    meeting_type: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    source_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    screenshot_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    summary: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    topics: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    pipeline_run_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("pipeline_runs.id"), nullable=True
    )
    scraped_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    board: Mapped["Board"] = relationship(back_populates="meetings")
    documents: Mapped[list["MeetingDocument"]] = relationship(back_populates="meeting", cascade="all, delete-orphan")


class MeetingDocument(Base):
    __tablename__ = "meeting_documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"))
    doc_type: Mapped[str] = mapped_column(String(20))  # "minutes", "agenda", "notice", "attachment"
    filename: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(Text)
    source_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    content_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    topics: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    scraped_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    meeting: Mapped["Meeting"] = relationship(back_populates="documents")
    pages: Mapped[list["DocumentPage"]] = relationship(back_populates="document", cascade="all, delete-orphan")


class PipelineRun(Base):
    __tablename__ = "pipeline_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    started_at: Mapped[datetime] = mapped_column(DateTime)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    status: Mapped[str] = mapped_column(String(20))  # "running", "completed", "failed"
    trigger: Mapped[str] = mapped_column(String(20))  # "manual", "scheduled"
    boards_collected: Mapped[int] = mapped_column(default=0)
    new_meetings_found: Mapped[int] = mapped_column(default=0)
    new_documents_found: Mapped[int] = mapped_column(default=0)
    boards_summarized: Mapped[int] = mapped_column(default=0)
    digest_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    report_path: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    log: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    events: Mapped[list["PipelineEvent"]] = relationship(
        back_populates="run", cascade="all, delete-orphan"
    )


class PipelineEvent(Base):
    __tablename__ = "pipeline_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("pipeline_runs.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime)
    stage: Mapped[str] = mapped_column(String(20))
    board_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    event_type: Mapped[str] = mapped_column(String(20))
    detail: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    run: Mapped["PipelineRun"] = relationship(back_populates="events")


class DocumentPage(Base):
    __tablename__ = "document_pages"

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("meeting_documents.id"))
    page_number: Mapped[int] = mapped_column()
    image_path: Mapped[str] = mapped_column(Text)
    thumb_path: Mapped[str] = mapped_column(Text)
    topics: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    tagged_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    rendered_at: Mapped[datetime] = mapped_column(DateTime)

    document: Mapped["MeetingDocument"] = relationship(back_populates="pages")


class MeetingIntelligence(Base):
    """Structured data extracted by AI from meeting minutes/agendas.
    One row per meeting — populated during Layer 2 pipeline processing."""
    __tablename__ = "meeting_intelligence"

    id: Mapped[int] = mapped_column(primary_key=True)
    meeting_id: Mapped[int] = mapped_column(ForeignKey("meetings.id"), unique=True)

    # Agenda & participation
    agenda_item_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    public_comment: Mapped[Optional[bool]] = mapped_column(nullable=True)
    attendance_count: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # Regulatory actions — structured from meeting content
    actions: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    # e.g. [{"type": "rule_adopted", "topic": "telehealth", "detail": "Expanded telehealth prescribing scope", "vote": "8-1"}]

    # Disciplinary actions
    disciplinary_actions: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    # e.g. [{"type": "license_revoked", "count": 3}, {"type": "fine", "count": 1, "total_amount": 25000}]

    # Topic posture — direction each topic is moving
    topic_postures: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    # e.g. {"telehealth": "expanding", "opioids": "restricting", "AI": "exploring"}

    # Legislative references
    legislation_refs: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    # e.g. [{"bill": "HB 1234", "status": "discussed", "topic": "scope-of-practice"}]

    # Key quotes or notable statements
    key_takeaways: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    # e.g. ["Board voted to require AI disclosure for telehealth visits starting Jan 2027"]

    # Processing metadata
    extracted_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    extraction_model: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)  # "claude-sonnet", "cowork", etc.

    meeting: Mapped["Meeting"] = relationship()


class IntelligenceBrief(Base):
    """Pre-generated intelligence briefs stored by the pipeline.
    The dashboard reads the latest one — no real-time AI calls needed."""
    __tablename__ = "intelligence_briefs"

    id: Mapped[int] = mapped_column(primary_key=True)
    period_label: Mapped[str] = mapped_column(String(50))  # "90-day", "monthly-2026-03", "weekly-2026-W14"
    brief_html: Mapped[str] = mapped_column(Text)
    meetings_analyzed: Mapped[int] = mapped_column(Integer, default=0)
    boards_covered: Mapped[int] = mapped_column(Integer, default=0)
    generated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    generated_by: Mapped[str] = mapped_column(String(50), default="cowork")  # "cowork", "claude-api", "manual"
    pipeline_run_id: Mapped[Optional[int]] = mapped_column(ForeignKey("pipeline_runs.id"), nullable=True)
