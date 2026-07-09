from fastapi import APIRouter
from app.modules.prediccion.schemas.prediccion_schema import PerfilEstudiante
from app.modules.prediccion.services.impl.prediccion_service_impl import PrediccionServiceImpl
from app.modules.prediccion.providers.impl.modelo_provider_impl import ModeloProviderImpl
from app.modules.prediccion.mappers.prediccion_mapper import PrediccionMapper
from app.core.responses.api_respuesta import ApiDeRespuesta
from app.core.responses.mensajes_confirmacion import MensajesDeConfirmacion
controlador = APIRouter()
proveedor_modelo = ModeloProviderImpl()
servicio_prediccion = PrediccionServiceImpl(modelo_provider=proveedor_modelo)

@controlador.post('/', response_model=None)
def predecir_desercion(perfil: PerfilEstudiante):
    estudiante_dominio = PrediccionMapper.a_dominio(perfil)
    resultado_dominio = servicio_prediccion.obtener_prediccion(estudiante_dominio)
    respuesta_dto = PrediccionMapper.a_dto(resultado_dominio)
    return ApiDeRespuesta.exito(mensaje_enum=MensajesDeConfirmacion.PREDICCION_EXITOSA, datos=respuesta_dto.model_dump())