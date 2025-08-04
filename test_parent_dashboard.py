import pytest

def test_parent_view_child_progress():
    child_data = {
        "name": "Alex",
        "level": 5,
        "power_points": 3200,
        "mood_trend": [3, 4, 5]
    }
    assert child_data["level"] >= 0
    assert isinstance(child_data["mood_trend"], list)

def test_parent_milestone_tracking():
    milestones = {"language": True, "motor": False}
    assert "language" in milestones
    assert isinstance(milestones["motor"], bool)