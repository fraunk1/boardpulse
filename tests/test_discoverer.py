"""Test meeting minutes page discovery logic."""
import pytest

from app.scraper.discoverer import score_link, pick_best_links


def test_score_high_relevance():
    assert score_link("Board Meeting Minutes", "/meetings/minutes") > 80


def test_score_medium_relevance():
    score = score_link("Public Meetings", "/public-meetings")
    assert 40 < score < 80


def test_score_low_relevance():
    score = score_link("Document Archive", "/documents")
    assert 0 < score < 40


def test_score_irrelevant():
    assert score_link("License Lookup", "/license-search") == 0


def test_score_ignores_external_links():
    assert score_link("Meeting Minutes", "https://twitter.com/board") == 0


def test_pick_best_links_sorted():
    links = [
        {"text": "License Lookup", "href": "/license"},
        {"text": "Board Meeting Minutes", "href": "/meetings/minutes"},
        {"text": "Calendar", "href": "/calendar"},
        {"text": "Public Meetings", "href": "/meetings"},
    ]
    best = pick_best_links(links, base_url="https://example.gov")
    assert len(best) > 0
    assert "minutes" in best[0]["href"]


def test_pick_best_links_empty_for_irrelevant():
    links = [
        {"text": "Home", "href": "/"},
        {"text": "Contact Us", "href": "/contact"},
        {"text": "FAQ", "href": "/faq"},
    ]
    best = pick_best_links(links, base_url="https://example.gov")
    assert len(best) == 0
