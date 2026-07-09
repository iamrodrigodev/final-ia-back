import os
import joblib
import pandas as pd
from app.modules.prediccion.domain.estudiante_dominio import EstudianteDominio, ResultadoDominio
from app.modules.prediccion.providers.modelo_provider import IModeloProvider
from app.core.exceptions.errores_personalizados import ExcepcionDeNegocio
from app.core.exceptions.mensajes_error import MensajesDeError

class ModeloProviderImpl(IModeloProvider):

    def __init__(self):
        self.ruta_modelo = os.path.join(os.path.dirname(__file__), '../../../../../models/pipeline_desercion.pkl')

    def ejecutar_prediccion(self, estudiante: EstudianteDominio) -> ResultadoDominio:
        if not os.path.exists(self.ruta_modelo):
            raise ExcepcionDeNegocio(MensajesDeError.MODELO_NO_ENTRENADO)
        try:
            pipeline = joblib.load(self.ruta_modelo)
            datos_diccionario = {'Marital status': estudiante.estado_civil, 'Application mode': estudiante.modo_aplicacion, 'Application order': estudiante.orden_aplicacion, 'Course': estudiante.curso, 'Daytime/evening attendance\t': estudiante.asistencia_diurna_nocturna, 'Previous qualification': estudiante.calificacion_previa, 'Admission grade': estudiante.nota_admision, 'Displaced': estudiante.desplazado, 'Educational special needs': estudiante.necesidades_educativas_especiales, 'Debtor': estudiante.deudor, 'Tuition fees up to date': estudiante.mensualidades_al_dia, 'Gender': estudiante.genero, 'Scholarship holder': estudiante.becario, 'Age at enrollment': estudiante.edad_al_matricularse, 'Curricular units 1st sem (enrolled)': estudiante.unidades_curriculares_1er_sem_inscritas, 'Curricular units 1st sem (evaluations)': estudiante.unidades_curriculares_1er_sem_evaluaciones, 'Curricular units 1st sem (approved)': estudiante.unidades_curriculares_1er_sem_aprobadas, 'Curricular units 1st sem (grade)': estudiante.unidades_curriculares_1er_sem_nota}
            datos_df = pd.DataFrame([datos_diccionario])
            prediccion = pipeline.predict(datos_df)[0]
            probabilidad_calculada = 0.0
            if hasattr(pipeline, 'predict_proba'):
                probabilidades = pipeline.predict_proba(datos_df)[0]
                clases = list(pipeline.classes_)
                if 1 in clases:
                    indice_dropout = clases.index(1)
                    probabilidad_calculada = probabilidades[indice_dropout]
                else:
                    probabilidad_calculada = probabilidades[1] if len(probabilidades) > 1 else 1.0
            clase_prediccion = 'Deserción' if prediccion == 1 else 'Graduado'
            return ResultadoDominio(prediccion=clase_prediccion, probabilidad=float(probabilidad_calculada), mensaje='Predicción procesada exitosamente por el modelo de IA.')
        except Exception as e:
            raise ExcepcionDeNegocio(MensajesDeError.ERROR_AL_PREDECIR, detalles=str(e))