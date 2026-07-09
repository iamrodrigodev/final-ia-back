from unittest.mock import patch, Mock
from app.modules.prediccion.providers.impl.modelo_provider_impl import ModeloProviderImpl

@patch("app.modules.prediccion.providers.impl.modelo_provider_impl.joblib.load")
@patch("os.path.exists", return_value=True)
def test_ejecutar_prediccion_una_sola_clase(mock_exists, mock_joblib_load, estudiante_dominio):
    # Simula un modelo que por algún motivo fue entrenado con una sola clase
    mock_model = Mock()
    mock_model.predict.return_value = [1]
    mock_model.predict_proba.return_value = [[1.0]] # Solo 1 probabilidad devuelta
    mock_model.classes_ = [1]
    mock_joblib_load.return_value = mock_model
    
    provider = ModeloProviderImpl()
    resultado = provider.ejecutar_prediccion(estudiante_dominio)
    
    assert resultado.prediccion == "Deserción"
    assert resultado.probabilidad == 1.0
