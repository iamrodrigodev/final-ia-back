from typing import Protocol
from app.modules.prediccion.domain.estudiante_dominio import EstudianteDominio, ResultadoDominio

class IModeloProvider(Protocol):
    def ejecutar_prediccion(self, estudiante: EstudianteDominio) -> ResultadoDominio: ...
