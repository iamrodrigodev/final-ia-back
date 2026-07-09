from app.modules.prediccion.mappers.prediccion_mapper import PrediccionMapper
from app.modules.prediccion.schemas.respuesta.prediccion_respuesta import PrediccionRespuesta

def test_mapper_a_dominio(perfil_valido):
    dominio = PrediccionMapper.a_dominio(perfil_valido)
    assert dominio.edad_al_matricularse == 20
    assert dominio.nota_admision == 150.0
    assert dominio.estado_civil == 1

def test_mapper_a_dto(resultado_exitoso):
    dto = PrediccionMapper.a_dto(resultado_exitoso)
    assert isinstance(dto, PrediccionRespuesta)
    assert dto.prediccion == "Graduado"
    assert dto.probabilidad == 0.85
