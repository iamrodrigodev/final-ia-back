import pytest
from app.modules.prediccion.schemas.prediccion_schema import PerfilEstudiante
from app.modules.prediccion.domain.estudiante_dominio import ResultadoDominio
from fastapi.testclient import TestClient
from main import aplicacion

@pytest.fixture
def cliente_api():
    return TestClient(aplicacion)

@pytest.fixture
def perfil_valido():
    return PerfilEstudiante(
        estado_civil=1,
        modo_aplicacion=1,
        orden_aplicacion=1,
        curso=1,
        asistencia_diurna_nocturna=1,
        calificacion_previa=1,
        nota_admision=150.0,
        desplazado=0,
        necesidades_educativas_especiales=0,
        deudor=0,
        mensualidades_al_dia=1,
        genero=1,
        becario=0,
        edad_al_matricularse=20,
        unidades_curriculares_1er_sem_inscritas=5,
        unidades_curriculares_1er_sem_evaluaciones=5,
        unidades_curriculares_1er_sem_aprobadas=5,
        unidades_curriculares_1er_sem_nota=15.0
    )

@pytest.fixture
def perfil_diccionario():
    return {
        "estado_civil": 1,
        "modo_aplicacion": 1,
        "orden_aplicacion": 1,
        "curso": 1,
        "asistencia_diurna_nocturna": 1,
        "calificacion_previa": 1,
        "nota_admision": 150.0,
        "desplazado": 0,
        "necesidades_educativas_especiales": 0,
        "deudor": 0,
        "mensualidades_al_dia": 1,
        "genero": 1,
        "becario": 0,
        "edad_al_matricularse": 20,
        "unidades_curriculares_1er_sem_inscritas": 5,
        "unidades_curriculares_1er_sem_evaluaciones": 5,
        "unidades_curriculares_1er_sem_aprobadas": 5,
        "unidades_curriculares_1er_sem_nota": 15.0
    }

@pytest.fixture
def estudiante_dominio(perfil_valido):
    from app.modules.prediccion.mappers.prediccion_mapper import PrediccionMapper
    return PrediccionMapper.a_dominio(perfil_valido)

@pytest.fixture
def resultado_exitoso():
    return ResultadoDominio(
        prediccion="Graduado",
        probabilidad=0.85,
        mensaje="Test mensaje"
    )
