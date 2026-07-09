from fastapi import APIRouter
from app.core.responses.api_respuesta import ApiDeRespuesta

enrutador_salud = APIRouter(prefix="/salud", tags=["Salud del Sistema"])

@enrutador_salud.get("/")
def verificar_salud():
    return ApiDeRespuesta.exito(mensaje_enum="La API se encuentra estable y operativa", datos={"estado": "ok"})
