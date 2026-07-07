from fastapi.testclient import TestClient

from civiscope.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item():
    response = client.get("/items/10?q=notebook")

    assert response.status_code == 200
    assert response.json() == {
        "item_id": 10,
        "q": "notebook",
    }

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}