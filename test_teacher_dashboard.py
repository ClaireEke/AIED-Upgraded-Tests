import pytest

def test_teacher_class_overview():
    students = ["Alex", "Jamie", "Taylor"]
    assert len(students) > 0, "No students found"

def test_teacher_behavior_log():
    behavior_log = {"Alex": ["focused", "helpful"]}
    assert "Alex" in behavior_log
    assert isinstance(behavior_log["Alex"], list)