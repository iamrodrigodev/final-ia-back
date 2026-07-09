from typing import Protocol
from app.modules.prediccion.domain.estudiante_dominio import EstudianteDominio, ResultadoDominio

class IPrediccionService(Protocol):
    def obtener_prediccion(self, estudiante: EstudianteDominio) -> ResultadoDominio: ...

