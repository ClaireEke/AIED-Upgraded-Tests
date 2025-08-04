import pytest

def test_login_valid_credentials():
    # Simulate login with valid credentials
    email = "user@example.com"
    password = "securePass123"
    assert len(email) > 5 and "@" in email
    assert len(password) >= 6

def test_login_invalid_email_format():
    email = "userexample.com"
    password = "securePass123"
    assert "@" in email, "Email format is invalid"

def test_login_short_password():
    password = "123"
    assert len(password) >= 6, "Password too short"

def test_signup_missing_fields():
    name = ""
    email = ""
    password = ""
    assert name and email and password, "Signup fields cannot be empty"