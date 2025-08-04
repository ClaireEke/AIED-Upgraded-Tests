import pytest

def test_student_dashboard_load():
    dashboard_data = {
        "level": 3,
        "xp": 1500,
        "quests": ["Math Adventure", "Reading Quest"],
        "badges": ["Math Wizard"]
    }
    assert dashboard_data["level"] >= 0
    assert isinstance(dashboard_data["quests"], list)
    assert "Math Wizard" in dashboard_data["badges"]

def test_student_mood_checkin():
    mood = "😊"
    valid_moods = ["😊", "😐", "😕", "😟", "🤔"]
    assert mood in valid_moods, "Invalid mood selected"

def test_student_quest_completion():
    quest_steps = ["step1", "step2", "step3"]
    completed_steps = ["step1", "step2"]
    assert len(completed_steps) < len(quest_steps), "Quest not fully completed"