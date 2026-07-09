from unittest.mock import patch
from app.core.responses.mensajes_confirmacion import MensajesDeConfirmacion
from app.core.exceptions.mensajes_error import MensajesDeError

def test_api_prediccion_datos_invalidos(cliente_api):
    # Enviar un tipo de dato erróneo para forzar RequestValidationError
    response = cliente_api.post("/api/prediccion/", json={"estado_civil": "invalido"})
    assert response.status_code == 400
    json_resp = response.json()
    assert json_resp["estado"] == 400
    assert json_resp["mensaje"] == MensajesDeError.DATOS_INVALIDOS.mensaje
    assert "errores" in json_resp

def test_api_prediccion_fuera_de_rango(cliente_api, perfil_diccionario):
    perfil_invalido = perfil_diccionario.copy()
    perfil_invalido["estado_civil"] = 999 # Fuera de límite (max 6)
    
    response = cliente_api.post("/api/prediccion/", json=perfil_invalido)
    assert response.status_code == 400
    assert "errores" in response.json()
    assert "estado_civil" in response.json()["errores"]

@patch("app.modules.prediccion.controllers.prediccion_controller.servicio_prediccion.obtener_prediccion")
def test_api_prediccion_exitoso(mock_obtener_prediccion, cliente_api, perfil_diccionario, resultado_exitoso):
    mock_obtener_prediccion.return_value = resultado_exitoso
    
    response = cliente_api.post("/api/prediccion/", json=perfil_diccionario)
    
    assert response.status_code == 200
    json_resp = response.json()
    assert json_resp["estado"] == 200
    assert json_resp["mensaje"] == MensajesDeConfirmacion.PREDICCION_EXITOSA.value
    assert json_resp["datos"]["prediccion"] == "Graduado"
    assert json_resp["datos"]["probabilidad"] == 0.85
