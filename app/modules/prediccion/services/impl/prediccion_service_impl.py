from app.modules.prediccion.domain.estudiante_dominio import EstudianteDominio, ResultadoDominio
from app.modules.prediccion.services.prediccion_service import IPrediccionService
from app.modules.prediccion.providers.modelo_provider import IModeloProvider
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

class PrediccionServiceImpl(IPrediccionService):

    def __init__(self, modelo_provider: IModeloProvider):
        self.modelo_provider = modelo_provider

    def obtener_prediccion(self, estudiante: EstudianteDominio) -> ResultadoDominio:
        try:
            return self.modelo_provider.ejecutar_prediccion(estudiante)
        except ExcepcionDeNegocio as e:
            raise e
        except Exception as e:
            raise ExcepcionDeNegocio(MensajesDeError.ERROR_AL_PREDECIR, detalles=str(e))