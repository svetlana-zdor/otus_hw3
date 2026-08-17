import pytest
import requests

# Base URL of the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


# Test case 1: GET request to get a single post
def test_get_single_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


# Test case 2: POST request to create a new post
def test_create_post():
    response = requests.post(
        f"{BASE_URL}/posts",
        json={"title": "foo", "body": "bar", "userId": 1},
    )
    assert response.status_code == 201

    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)


# Test case 3: GET request to get a non-existent post
def test_get_nonexistent_post():
    response = requests.get(f"{BASE_URL}/posts/999999")
    assert response.status_code == 404