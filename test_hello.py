import pytest
import json

from hello import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"This is the main page!" in response.data

def test_greed_default(client):
    response = client.get("/greed/")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {"message": "Hello, World!"}

def test_greed_with_name(client):
    name = "Alice"
    response = client.get(f"/greed/{name}")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {"message": f"Hello, {name}!"}

def test_404_error_handler(client):
    response = client.get("/nonexistentpath")
    assert response.status_code == 200
    assert b"/nonexistentpath is not working" in response.data