from enum import Enum

class MensajesDeError(Enum):
    DATOS_INVALIDOS = ('Datos de entrada inválidos', 400)
    NO_AUTORIZADO = ('No autorizado', 401)
    ACCESO_DENEGADO = ('Acceso denegado', 403)
    ERROR_INTERNO = ('Error interno del servidor', 500)
    RECURSO_NO_ENCONTRADO = ('Recurso no encontrado', 404)
    MODELO_NO_ENTRENADO = ('El modelo de Machine Learning no ha sido entrenado o no existe.', 500)
    ERROR_AL_PREDECIR = ('Ocurrió un error procesando los datos para la predicción.', 500)

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo