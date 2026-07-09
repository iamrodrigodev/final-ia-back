import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from app.core.exceptions.excepciones_globales import registrar_manejadores_error
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

app_test = FastAPI()
registrar_manejadores_error(app_test)

@app_test.get("/error-negocio")
def ruta_error_negocio():
    raise ExcepcionDeNegocio(MensajesDeError.DATOS_INVALIDOS)

@app_test.get("/error-http")
def ruta_error_http():
    raise HTTPException(status_code=403, detail="Prohibido")

@app_test.get("/error-value")
def ruta_error_value():
    raise ValueError("Valor malo")

@app_test.get("/error-generico")
def ruta_error_generico():
    raise Exception("Algo explotó")

client = TestClient(app_test)

def test_manejador_excepcion_negocio():
    response = client.get("/error-negocio")
    assert response.status_code == 400
    assert response.json()["mensaje"] == "Datos de entrada inválidos"

def test_manejador_excepcion_http():
    response = client.get("/error-http")
    assert response.status_code == 403
    assert response.json()["mensaje"] == "Prohibido"

def test_manejador_value_error():
    response = client.get("/error-value")
    assert response.status_code == 400
    assert response.json()["mensaje"] == "Error de validación o valor incorrecto."

def test_manejador_excepcion_generica():
    response = client.get("/error-generico")
    assert response.status_code == 500
    assert "Error interno del servidor" in response.json()["mensaje"]
