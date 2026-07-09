import pytest
import json
from app.core.responses.api_respuesta import ApiDeRespuesta
from app.core.responses.mensajes_confirmacion import MensajesDeConfirmacion

def test_api_respuesta_exito_paginado():
    # Simular una respuesta paginada
    resp = ApiDeRespuesta.exito_paginado(
        mensaje_enum=MensajesDeConfirmacion.PREDICCION_EXITOSA,
        datos=[{"id": 1}],
        total=1,
        pagina=1,
        tamano_pagina=10,
        total_paginas=1
    )
    assert resp.status_code == 200
    body = json.loads(resp.body.decode())
    assert body["datos"] == [{"id": 1}]
    assert body["paginacion"]["total"] == 1
    assert body["paginacion"]["pagina"] == 1

def test_api_respuesta_error_custom_status():
    from app.core.exceptions.mensajes_error import MensajesDeError
    resp = ApiDeRespuesta.error(
        mensaje_enum=MensajesDeError.DATOS_INVALIDOS,
        codigo=418 # I'm a teapot
    )
    assert resp.status_code == 418
    body = json.loads(resp.body.decode())
    assert body["estado"] == 418
