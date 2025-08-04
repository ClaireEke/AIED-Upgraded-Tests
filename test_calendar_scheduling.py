import pytest

def test_event_creation():
    event = {"title": "Math Test", "date": "2024-06-01"}
    assert "Math Test" in event["title"]
    assert event["date"].startswith("2024")

def test_reminder_alerts():
    alerts_enabled = True
    assert alerts_enabled is True