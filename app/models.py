"""SQLAlchemy models for boardpulse."""
from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import String, Text, Date, DateTime, ForeignKey
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
    scraped_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    meeting: Mapped["Meeting"] = relationship(back_populates="documents")
