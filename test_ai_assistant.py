import pytest

def test_ai_math_query():
    query = "What is 84 ÷ 4?"
    assert query.endswith("?"), "Query should be a question"

def test_ai_image_upload():
    image_uploaded = True
    image_format = "jpg"
    assert image_uploaded and image_format in ["jpg", "png"], "Invalid image format"

def test_ai_response_followup():
    response = "Let's break this down step by step."
    assert "step" in response, "Response should include step-by-step explanation"