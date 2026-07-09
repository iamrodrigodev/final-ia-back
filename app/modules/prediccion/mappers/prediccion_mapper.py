from app.modules.prediccion.schemas.peticion.prediccion_peticion import PrediccionPeticion
from app.modules.prediccion.schemas.respuesta.prediccion_respuesta import PrediccionRespuesta
from app.modules.prediccion.domain.estudiante_dominio import EstudianteDominio, ResultadoDominio

class PrediccionMapper:

    @staticmethod
    def a_dominio(perfil_dto: PrediccionPeticion) -> EstudianteDominio:
        return EstudianteDominio(estado_civil=perfil_dto.estado_civil, modo_aplicacion=perfil_dto.modo_aplicacion, orden_aplicacion=perfil_dto.orden_aplicacion, curso=perfil_dto.curso, asistencia_diurna_nocturna=perfil_dto.asistencia_diurna_nocturna, calificacion_previa=perfil_dto.calificacion_previa, nota_admision=perfil_dto.nota_admision, desplazado=perfil_dto.desplazado, necesidades_educativas_especiales=perfil_dto.necesidades_educativas_especiales, deudor=perfil_dto.deudor, mensualidades_al_dia=perfil_dto.mensualidades_al_dia, genero=perfil_dto.genero, becario=perfil_dto.becario, edad_al_matricularse=perfil_dto.edad_al_matricularse, unidades_curriculares_1er_sem_inscritas=perfil_dto.unidades_curriculares_1er_sem_inscritas, unidades_curriculares_1er_sem_evaluaciones=perfil_dto.unidades_curriculares_1er_sem_evaluaciones, unidades_curriculares_1er_sem_aprobadas=perfil_dto.unidades_curriculares_1er_sem_aprobadas, unidades_curriculares_1er_sem_nota=perfil_dto.unidades_curriculares_1er_sem_nota)

    @staticmethod
    def a_dto(resultado_dominio: ResultadoDominio) -> PrediccionRespuesta:
        return PrediccionRespuesta(prediccion=resultado_dominio.prediccion, probabilidad=resultado_dominio.probabilidad, mensaje=resultado_dominio.mensaje)