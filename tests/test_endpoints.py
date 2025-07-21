# Tests for FastAPI endpoints
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_colorize_endpoint():
    with open("static/sample.jpg", "rb") as img:
        response = client.post(
            "/colorize",
            files={"image": ("filename.jpg", img, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")

def test_cartoonize_endpoint():
    with open("static/sample.jpg", "rb") as img:
        response = client.post(
            "/cartoonize",
            files={"image": ("filename.jpg", img, "image/jpeg")}
        )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("image/")
