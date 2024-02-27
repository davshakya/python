import pytest
import requests

@pytest.fixture
def base_url():
    return "https://api.example.com"

@pytest.fixture
def setup_teardown():
    # Setup code (if needed)
    yield
    # Teardown code (if needed)

def test_get_request(base_url, setup_teardown):
    url = f"{base_url}/endpoint"
    response = requests.get(url)

    # Example assertion, modify as needed
    assert response.status_code == 200
    assert "expected_content" in response.text

def test_post_request(base_url, setup_teardown):
    url = f"{base_url}/endpoint"
    payload = {"key": "value"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    # Example assertion, modify as needed
    assert response.status_code == 201
    assert "created_id" in response.text
