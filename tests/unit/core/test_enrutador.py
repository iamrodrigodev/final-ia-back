import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.api.enrutador import registrar_rutas

app_test = FastAPI()
registrar_rutas(app_test)
client = TestClient(app_test)

def test_api_enrutador_inclusiones():
    # Verifica que el enrutador haya cargado las rutas (debería dar Method Not Allowed en vez de Not Found si existe)
    # o devolver el error normal de validacion
    response = client.post("/api/prediccion/", json={})
    assert response.status_code in [400, 422, 405]  # Significa que la ruta existe
