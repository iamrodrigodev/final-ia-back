class EstudianteDominio:

    def __init__(self, estado_civil: int, modo_aplicacion: int, orden_aplicacion: int, curso: int, asistencia_diurna_nocturna: int, calificacion_previa: int, nota_admision: float, desplazado: int, necesidades_educativas_especiales: int, deudor: int, mensualidades_al_dia: int, genero: int, becario: int, edad_al_matricularse: int, unidades_curriculares_1er_sem_inscritas: int, unidades_curriculares_1er_sem_evaluaciones: int, unidades_curriculares_1er_sem_aprobadas: int, unidades_curriculares_1er_sem_nota: float):
        self.estado_civil = estado_civil
        self.modo_aplicacion = modo_aplicacion
        self.orden_aplicacion = orden_aplicacion
        self.curso = curso
        self.asistencia_diurna_nocturna = asistencia_diurna_nocturna
        self.calificacion_previa = calificacion_previa
        self.nota_admision = nota_admision
        self.desplazado = desplazado
        self.necesidades_educativas_especiales = necesidades_educativas_especiales
        self.deudor = deudor
        self.mensualidades_al_dia = mensualidades_al_dia
        self.genero = genero
        self.becario = becario
        self.edad_al_matricularse = edad_al_matricularse
        self.unidades_curriculares_1er_sem_inscritas = unidades_curriculares_1er_sem_inscritas
        self.unidades_curriculares_1er_sem_evaluaciones = unidades_curriculares_1er_sem_evaluaciones
        self.unidades_curriculares_1er_sem_aprobadas = unidades_curriculares_1er_sem_aprobadas
        self.unidades_curriculares_1er_sem_nota = unidades_curriculares_1er_sem_nota

class ResultadoDominio:

    def __init__(self, prediccion: str, probabilidad: float, mensaje: str):
        self.prediccion = prediccion
        self.probabilidad = probabilidad
        self.mensaje = mensaje