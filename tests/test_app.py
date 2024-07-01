import pytest
from app import ask_question

# Setup
@pytest.fixture
def mock_successful_response(monkeypatch):
    def mock_post(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200
                self.text = '{"answer": "42"}'

            def json(self):
                return {"answer": "42"}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

@pytest.fixture
def mock_error_response(monkeypatch):
    def mock_post(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 400
                self.text = '{"error": "Bad request"}'

            def json(self):
                return {"error": "Bad request"}
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

# Tests
def test_ask_question_success(mock_successful_response):
    result = ask_question("org123", "proj123", "What is the meaning of life?")
    assert result == {"answer": "42"}, "The function should return the correct answer from the API."

def test_ask_question_error(mock_error_response):
    result = ask_question("org123", "proj123", "Invalid question")
    assert "error" in result, "The function should return an error message for a failed API call."
