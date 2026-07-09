import pytest
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

def test_excepcion_de_negocio():
    exc = ExcepcionDeNegocio(MensajesDeError.DATOS_INVALIDOS, detalles="Prueba detalle")
    assert exc.mensaje_enum == MensajesDeError.DATOS_INVALIDOS
    assert exc.detalles == "Prueba detalle"
    assert "Datos de entrada inválidos" in str(exc)
