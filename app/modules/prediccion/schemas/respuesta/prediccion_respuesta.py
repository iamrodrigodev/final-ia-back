from pydantic import BaseModel, Field

class PrediccionRespuesta(BaseModel):
    prediccion: str = Field(..., min_length=1, description="Predicción de deserción ('Deserción' o 'Graduado')")
    probabilidad: float = Field(..., ge=0.0, le=1.0, description='Probabilidad de la predicción (0-1)')
    mensaje: str = Field(..., min_length=1, description='Mensaje adicional sobre la predicción')
