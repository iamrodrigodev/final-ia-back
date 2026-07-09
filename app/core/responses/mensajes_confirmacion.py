from enum import Enum

class MensajesDeConfirmacion(Enum):
    PREDICCION_EXITOSA = "Predicción realizada correctamente."
    MODELO_CARGADO = "Modelo de IA cargado y listo."

    def __init__(self, mensaje):
        self.mensaje = mensaje
