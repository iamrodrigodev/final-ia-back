import pytest
from unittest.mock import Mock
from app.modules.prediccion.services.impl.prediccion_service_impl import PrediccionServiceImpl
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

def test_obtener_prediccion_exitoso(estudiante_dominio, resultado_exitoso):
    mock_provider = Mock()
    mock_provider.ejecutar_prediccion.return_value = resultado_exitoso
    
    servicio = PrediccionServiceImpl(modelo_provider=mock_provider)
    resultado = servicio.obtener_prediccion(estudiante_dominio)
    
    assert resultado.prediccion == "Graduado"
    mock_provider.ejecutar_prediccion.assert_called_once_with(estudiante_dominio)

def test_obtener_prediccion_propaga_excepcion_negocio(estudiante_dominio):
    mock_provider = Mock()
    mock_provider.ejecutar_prediccion.side_effect = ExcepcionDeNegocio(MensajesDeError.MODELO_NO_ENTRENADO)
    
    servicio = PrediccionServiceImpl(modelo_provider=mock_provider)
    
    with pytest.raises(ExcepcionDeNegocio) as exc_info:
        servicio.obtener_prediccion(estudiante_dominio)
    
    assert exc_info.value.mensaje_enum == MensajesDeError.MODELO_NO_ENTRENADO

def test_obtener_prediccion_captura_y_lanza_excepcion_generica(estudiante_dominio):
    mock_provider = Mock()
    mock_provider.ejecutar_prediccion.side_effect = Exception("Fallo en red neuronal")
    
    servicio = PrediccionServiceImpl(modelo_provider=mock_provider)
    
    with pytest.raises(ExcepcionDeNegocio) as exc_info:
        servicio.obtener_prediccion(estudiante_dominio)
    
    assert exc_info.value.mensaje_enum == MensajesDeError.ERROR_AL_PREDECIR
    assert "Fallo en red neuronal" in str(exc_info.value.detalles)
