"""SQLAlchemy models for boardpulse."""
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import String, Text, Date, DateTime, ForeignKey, JSON
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
