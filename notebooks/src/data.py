import pandas as pd
from notebooks.src.config import RUTA_DATOS

def fase_1_obtencion_de_datos() -> pd.DataFrame:
    print("\n=== FASE 1: OBTENCIÓN DE DATOS ===")
    datos = pd.read_csv(RUTA_DATOS, sep=";")
    print(f"Dataset cargado exitosamente. Dimensiones: {datos.shape}")
    return datos
