"""Tests for the summarizer data bundle preparation."""
import pytest
from datetime import date, timedelta

from app.extractor.prompts import per_board_prompt, national_synthesis_prompt


class TestPerBoardPrompt:
    """Test per-board prompt template generation."""

    def test_basic_prompt_structure(self):
        """Prompt includes board name, state, and meeting data."""
        meetings = [
            {
                "meeting_date": "2026-01-15",
                "title": "Regular Board Meeting",
                "documents": [
                    {
                        "doc_type": "minutes",
                        "filename": "jan_minutes.pdf",
                        "content_text": "The board discussed telehealth regulations.",
                    }
                ],
            }
        ]
        result = per_board_prompt(
            board_name="Medical Board of California",
            state="CA",
            board_code="CA_MD",
            meetings=meetings,
        )
        assert "Medical Board of California" in result
        assert "CA" in result
        assert "CA_MD" in result
        assert "2026-01-15" in result
        assert "telehealth regulations" in result

    def test_multiple_meetings(self):
        """Prompt includes all meetings."""
        meetings = [
            {
                "meeting_date": "2026-01-15",
                "title": "January Meeting",
                "documents": [
                    {
                        "doc_type": "minutes",
                        "filename": "jan.pdf",
                        "content_text": "January discussion.",
                    }
                ],
            },
            {
                "meeting_date": "2026-02-15",
                "title": "February Meeting",
                "documents": [
                    {
                        "doc_type": "minutes",
                        "filename": "feb.pdf",
                        "content_text": "February discussion.",
                    }
                ],
            },
        ]
        result = per_board_prompt(
            board_name="Test Board",
            state="TX",
            board_code="TX_MD",
            meetings=meetings,
        )
        assert "January discussion" in result
        assert "February discussion" in result
        assert "2026-01-15" in result
        assert "2026-02-15" in result

    def test_meeting_without_text(self):
        """Meetings with no extracted text show placeholder."""
        meetings = [
            {
                "meeting_date": "2026-03-01",
                "title": "March Meeting",
                "documents": [
                    {
                        "doc_type": "minutes",
                        "filename": "march.pdf",
                        "content_text": None,
                    }
                ],
            }
        ]
        result = per_board_prompt(
            board_name="Test Board",
            state="FL",
            board_code="FL_MD",
            meetings=meetings,
        )
        assert "No extracted text available" in result

    def test_prompt_includes_instructions(self):
        """Prompt includes the analysis instructions."""
        meetings = [
            {
                "meeting_date": "2026-01-01",
                "title": "Test",
                "documents": [],
            }
        ]
        result = per_board_prompt(
            board_name="Test Board",
            state="NY",
            board_code="NY_MD",
            meetings=meetings,
        )
        assert "Key Topics Discussed" in result
        assert "Notable Actions" in result
        assert "Recurring Themes" in result
        assert "Noteworthy Items" in result

    def test_multiple_documents_per_meeting(self):
        """Multiple documents in one meeting are all included."""
        meetings = [
            {
                "meeting_date": "2026-01-15",
                "title": "Board Meeting",
                "documents": [
                    {
                        "doc_type": "minutes",
                        "filename": "minutes.pdf",
                        "content_text": "Full minutes text here.",
                    },
                    {
                        "doc_type": "agenda",
                        "filename": "agenda.pdf",
                        "content_text": "Agenda items listed.",
                    },
                ],
            }
        ]
        result = per_board_prompt(
            board_name="Test Board",
            state="OH",
            board_code="OH_MD",
            meetings=meetings,
        )
        assert "Full minutes text here" in result
        assert "Agenda items listed" in result
        assert "[MINUTES]" in result
        assert "[AGENDA]" in result


class TestNationalSynthesisPrompt:
    """Test national synthesis prompt template generation."""

    def test_basic_synthesis_structure(self):
        """Synthesis prompt includes all board summaries."""
        summaries = [
            {
                "board_name": "Medical Board of California",
                "state": "CA",
                "board_code": "CA_MD",
                "summary_text": "California discussed telehealth and AI.",
            },
            {
                "board_name": "Texas Medical Board",
                "state": "TX",
                "board_code": "TX_MD",
                "summary_text": "Texas focused on licensing reform.",
            },
        ]
        result = national_synthesis_prompt(summaries, date(2026, 3, 29))
        assert "Medical Board of California" in result
        assert "Texas Medical Board" in result
        assert "telehealth and AI" in result
        assert "licensing reform" in result
        assert "2026-03-29" in result
        assert "2" in result  # board count

    def test_states_listed(self):
        """Synthesis prompt lists covered states."""
        summaries = [
            {
                "board_name": "Board A",
                "state": "CA",
                "board_code": "CA_MD",
                "summary_text": "Summary A.",
            },
            {
                "board_name": "Board B",
                "state": "NY",
                "board_code": "NY_MD",
                "summary_text": "Summary B.",
            },
        ]
        result = national_synthesis_prompt(summaries, date(2026, 3, 29))
        assert "CA, NY" in result

    def test_synthesis_instructions(self):
        """Synthesis prompt includes the correct analysis sections."""
        summaries = [
            {
                "board_name": "Board",
                "state": "FL",
                "board_code": "FL_MD",
                "summary_text": "Test.",
            },
        ]
        result = national_synthesis_prompt(summaries, date(2026, 3, 29))
        assert "Top Topics Nationally" in result
        assert "Regional Patterns" in result
        assert "Emerging Trends" in result
        assert "Notable Outliers" in result
        assert "Recommendations for FSMB" in result
