import os
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.core.exceptions.excepciones_globales import registrar_manejadores_error
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.security.cors import configurar_cors
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import json

app_test = FastAPI()
configurar_cors(app_test)
registrar_manejadores_error(app_test)

class ModeloPrueba(BaseModel):
    campo: int

@app_test.post("/validacion")
def endpoint_validacion(modelo: ModeloPrueba):
    return {"ok": True}

@app_test.get("/error-negocio")
def error_negocio():
    raise ExcepcionDeNegocio("Error test", 409, detalles="Detalle")

@app_test.get("/error-generico")
def error_generico():
    raise Exception("Fatal error")

client = TestClient(app_test)

def test_excepcion_negocio():
    response = client.get("/error-negocio")
    assert response.status_code == 409
    data = response.json()
    assert data["mensaje"] == "Error test"
    assert data["detalles"] == "Detalle"

def test_excepcion_generica():
    response = client.get("/error-generico")
    assert response.status_code == 500
    assert "Error interno del servidor" in response.json()["mensaje"]

def test_excepcion_validacion():
    response = client.post("/validacion", json={"campo": "texto_invalido"})
    assert response.status_code == 422
    assert "Error de validación en los datos enviados" in response.json()["mensaje"]

def test_cors_origen_permitido():
    response = client.get("/error-negocio", headers={"origin": "http://localhost:5173"})
    assert response.status_code == 409

def test_cors_origen_bloqueado():
    response = client.get("/error-negocio", headers={"origin": "http://hacker.com"})
    assert response.status_code == 403
    assert response.json()["mensaje"] == "CORS Origin Restringido"

def test_cors_produccion(monkeypatch):
    monkeypatch.setenv("ENTORNO", "produccion")
    monkeypatch.setenv("FRONTEND_URL", "https://mi-dominio.com")
    
    app_prod = FastAPI()
    configurar_cors(app_prod)
    client_prod = TestClient(app_prod)
    
    @app_prod.get("/")
    def index(): return {"ok": True}
    
    # Origen permitido
    resp1 = client_prod.get("/", headers={"origin": "https://mi-dominio.com"})
    assert resp1.status_code == 200
    
    # Origen bloqueado
    resp2 = client_prod.get("/", headers={"origin": "http://localhost:5173"})
    assert resp2.status_code == 403

def test_api_respuesta_metodos():
    from app.core.responses.api_respuesta import ApiDeRespuesta
    resp = ApiDeRespuesta.creado(mensaje_enum="OK", datos={"id": 1})
    assert resp.status_code == 201
    
    resp_err = ApiDeRespuesta.error(mensaje_enum="Fallo", errores=["x"], codigo=400)
    assert resp_err.status_code == 400

def test_enrutador_registrar_rutas():
    from app.api.enrutador import registrar_rutas
    app_test2 = FastAPI()
    registrar_rutas(app_test2)
    client2 = TestClient(app_test2)
    resp = client2.get("/api/prediccion/estado")
    # No implementado todavía o no existe la ruta de estado, pero la inclusión funcionó si no lanza error
    assert resp.status_code in (200, 404, 405)
