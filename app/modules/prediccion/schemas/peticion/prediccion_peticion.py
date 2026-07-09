from pydantic import BaseModel, Field, field_validator
from app.modules.prediccion.schemas.validaciones import (
    validar_estado_civil, validar_modo_aplicacion, validar_orden_aplicacion,
    validar_curso, validar_booleano, validar_calificacion_previa,
    validar_nota_admision, validar_edad, validar_unidades, validar_nota_semestre
)

class PrediccionPeticion(BaseModel):
    estado_civil: int = Field(default=1, description='Estado Civil (1-6)')
    modo_aplicacion: int = Field(default=1, description='Modo de aplicación')
    orden_aplicacion: int = Field(default=1, description='Orden de aplicación (0-9)')
    curso: int = Field(default=1, description='Curso inscrito')
    asistencia_diurna_nocturna: int = Field(default=1, description='Asistencia diurna/nocturna (0 o 1)')
    calificacion_previa: int = Field(default=1, description='Calificación previa')
    nota_admision: float = Field(default=120.0, description='Nota de admisión (0-200)')
    desplazado: int = Field(default=0, description='Estudiante desplazado (0 o 1)')
    necesidades_educativas_especiales: int = Field(default=0, description='Necesidades educativas especiales (0 o 1)')
    deudor: int = Field(default=0, description='Deudor financiero (0 o 1)')
    mensualidades_al_dia: int = Field(default=1, description='Mensualidades al día (0 o 1)')
    genero: int = Field(default=0, description='Género (0 o 1)')
    becario: int = Field(default=0, description='Es becario (0 o 1)')
    edad_al_matricularse: int = Field(default=20, description='Edad al matricularse (15-100)')
    unidades_curriculares_1er_sem_inscritas: int = Field(default=5, description='Unidades curriculares inscritas en el 1er semestre')
    unidades_curriculares_1er_sem_evaluaciones: int = Field(default=5, description='Evaluaciones cursadas en el 1er semestre')
    unidades_curriculares_1er_sem_aprobadas: int = Field(default=5, description='Unidades curriculares aprobadas en el 1er semestre')
    unidades_curriculares_1er_sem_nota: float = Field(default=13.0, description='Nota promedio en el 1er semestre (0-20)')

    @field_validator('estado_civil')
    @classmethod
    def val_estado_civil(cls, v): return validar_estado_civil(v)

    @field_validator('modo_aplicacion')
    @classmethod
    def val_modo_aplicacion(cls, v): return validar_modo_aplicacion(v)

    @field_validator('orden_aplicacion')
    @classmethod
    def val_orden_aplicacion(cls, v): return validar_orden_aplicacion(v)

    @field_validator('curso')
    @classmethod
    def val_curso(cls, v): return validar_curso(v)

    @field_validator('asistencia_diurna_nocturna', 'desplazado', 'necesidades_educativas_especiales', 'deudor', 'mensualidades_al_dia', 'genero', 'becario')
    @classmethod
    def val_booleano(cls, v): return validar_booleano(v)

    @field_validator('calificacion_previa')
    @classmethod
    def val_calificacion_previa(cls, v): return validar_calificacion_previa(v)

    @field_validator('nota_admision')
    @classmethod
    def val_nota_admision(cls, v): return validar_nota_admision(v)

    @field_validator('edad_al_matricularse')
    @classmethod
    def val_edad(cls, v): return validar_edad(v)

    @field_validator('unidades_curriculares_1er_sem_inscritas', 'unidades_curriculares_1er_sem_evaluaciones', 'unidades_curriculares_1er_sem_aprobadas')
    @classmethod
    def val_unidades(cls, v): return validar_unidades(v)

    @field_validator('unidades_curriculares_1er_sem_nota')
    @classmethod
    def val_nota_semestre(cls, v): return validar_nota_semestre(v)
