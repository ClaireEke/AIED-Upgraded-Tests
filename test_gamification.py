import pytest

def test_quest_completion():
    quest = {"steps_completed": 4, "total_steps": 4}
    assert quest["steps_completed"] == quest["total_steps"]

def test_rewards_distribution():
    rewards = {"power_points": 500, "coins": 100, "badge": "Math Explorer"}
    assert rewards["power_points"] > 0
    assert rewards["coins"] > 0
    assert isinstance(rewards["badge"], str)