from fastapi.testclient import TestClient
from app.main import app   # Đảm bảo đường dẫn đúng

client = TestClient(app)

def test_create_task(app):
    response = client.post("/tasks/", json={"title": "thien", "description": "test1", "completed": False})
    assert response.status_code == 200
    assert response.json()["title"] == "thien"