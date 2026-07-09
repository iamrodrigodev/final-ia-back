import pytest
from fastapi.testclient import TestClient
from main import aplicacion

client = TestClient(aplicacion)

def test_api_salud_estable():
    response = client.get("/api/salud/")
    assert response.status_code == 200
    data = response.json()
    assert data["estado"] == 200
    assert data["mensaje"] == "La API se encuentra estable y operativa"
    assert data["datos"]["estado"] == "ok"
