import pytest

def test_message_content_filter():
    message = "You are stupid"
    banned_words = ["stupid", "hate"]
    assert not any(word in message for word in banned_words), "Inappropriate content detected"

def test_message_attachment_format():
    attachment_format = "pdf"
    assert attachment_format in ["pdf", "docx", "jpg", "png"], "Unsupported attachment format"