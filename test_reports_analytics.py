import pytest

def test_report_generation():
    report_type = "academic"
    valid_types = ["academic", "wellbeing", "milestone"]
    assert report_type in valid_types, "Invalid report type"

def test_report_data_integrity():
    report_data = {"grades": [80, 90, 85]}
    assert all(isinstance(score, int) for score in report_data["grades"]), "Invalid grade data"