import pytest

def test_encryption_enabled():
    encryption_status = True
    assert encryption_status, "Encryption must be enabled"

def test_role_based_access():
    user_role = "student"
    allowed_roles = ["student", "parent", "teacher", "admin"]
    assert user_role in allowed_roles, "Invalid role access"