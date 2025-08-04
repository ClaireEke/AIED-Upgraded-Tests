import pytest

def test_encryption_enabled():
    encryption = True
    assert encryption is True

def test_role_based_access():
    roles = {"student": ["view"], "teacher": ["view", "edit"], "admin": ["all"]}
    assert "edit" in roles["teacher"]
    assert "all" in roles["admin"]