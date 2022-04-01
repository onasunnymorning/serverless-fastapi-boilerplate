from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_get_hello():
    response = client.get("/api/v1/hello/mais")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello mais"}