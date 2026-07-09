import pytest
from unittest.mock import patch, Mock
from app.modules.prediccion.providers.impl.modelo_provider_impl import ModeloProviderImpl
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

def test_ejecutar_prediccion_modelo_no_existe(estudiante_dominio):
    provider = ModeloProviderImpl()
    with patch("os.path.exists", return_value=False):
        with pytest.raises(ExcepcionDeNegocio) as exc_info:
            provider.ejecutar_prediccion(estudiante_dominio)
        assert exc_info.value.mensaje_enum == MensajesDeError.MODELO_NO_ENTRENADO

@patch("app.modules.prediccion.providers.impl.modelo_provider_impl.joblib.load")
@patch("os.path.exists", return_value=True)
def test_ejecutar_prediccion_exitoso_dropout(mock_exists, mock_joblib_load, estudiante_dominio):
    # Mocking the model
    mock_model = Mock()
    mock_model.predict.return_value = [1] # 1 es Deserción
    mock_model.predict_proba.return_value = [[0.1, 0.9]] # Alta probabilidad de deserción
    mock_model.classes_ = [0, 1]
    mock_joblib_load.return_value = mock_model
    
    provider = ModeloProviderImpl()
    resultado = provider.ejecutar_prediccion(estudiante_dominio)
    
    assert resultado.prediccion == "Deserción"
    assert resultado.probabilidad == 0.9

@patch("app.modules.prediccion.providers.impl.modelo_provider_impl.joblib.load")
@patch("os.path.exists", return_value=True)
def test_ejecutar_prediccion_exitoso_graduate(mock_exists, mock_joblib_load, estudiante_dominio):
    mock_model = Mock()
    mock_model.predict.return_value = [0] # 0 es Graduado
    mock_model.predict_proba.return_value = [[0.8, 0.2]]
    mock_model.classes_ = [0, 1]
    mock_joblib_load.return_value = mock_model
    
    provider = ModeloProviderImpl()
    resultado = provider.ejecutar_prediccion(estudiante_dominio)
    
    assert resultado.prediccion == "Graduado"
    assert resultado.probabilidad == 0.2 # Probabilidad de deserción es la clase 1

@patch("app.modules.prediccion.providers.impl.modelo_provider_impl.joblib.load")
@patch("os.path.exists", return_value=True)
def test_ejecutar_prediccion_lanza_error_prediccion(mock_exists, mock_joblib_load, estudiante_dominio):
    mock_model = Mock()
    mock_model.predict.side_effect = Exception("Error pandas")
    mock_joblib_load.return_value = mock_model
    
    provider = ModeloProviderImpl()
    with pytest.raises(ExcepcionDeNegocio) as exc_info:
        provider.ejecutar_prediccion(estudiante_dominio)
    
    assert exc_info.value.mensaje_enum == MensajesDeError.ERROR_AL_PREDECIR
