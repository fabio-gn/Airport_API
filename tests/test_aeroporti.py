from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Airport API is running"}


def test_get_airports():
    response = client.get("/aeroporti")
    assert response.status_code == 200
    data = response.json()
    assert "page" in data
    assert "size" in data
    assert "total" in data
    assert "data" in data


def test_get_airports_pagination():
    response = client.get("/aeroporti?page=1&size=2")
    assert response.status_code == 200
    data = response.json()
    assert data["page"] == 1
    assert data["size"] == 2
    assert len(data["data"]) == 2


def test_get_airport_success():
    response = client.get("/aeroporti/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_airport_not_found():
    response = client.get("/aeroporti/999")
    assert response.status_code == 404


def test_create_airport():
    payload = {"codice": "NAP", "citta": "Napoli"}
    response = client.post("/aeroporti", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["codice"] == "NAP"
    assert "id" in data


def test_create_airport_invalid_codice():
    payload = {"codice": "NA", "citta": "Napoli"}
    response = client.post("/aeroporti", json=payload)
    assert response.status_code == 422


def test_delete_airport():
    response = client.delete("/aeroporti/1")
    assert response.status_code == 204


def test_delete_airport_not_found():
    response = client.delete("/aeroporti/999")
    assert response.status_code == 404