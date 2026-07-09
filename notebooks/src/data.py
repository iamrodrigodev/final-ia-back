import os
import pandas as pd
from ucimlrepo import fetch_ucirepo
from notebooks.src.config import RUTA_DATOS

def fase_1_obtencion_de_datos() -> pd.DataFrame:
    print('\n=== FASE 1: OBTENCIÓN DE DATOS ===')
    
    # Si el archivo ya existe, lo cargamos
    if os.path.exists(RUTA_DATOS):
        print(f'  -> El dataset ya existe en {RUTA_DATOS}. Cargando archivo local...')
        datos = pd.read_csv(RUTA_DATOS, sep=';')
    else:
        print('  -> Descargando dataset oficial desde UCI Machine Learning Repository (ID: 697)...')
        dataset_uci = fetch_ucirepo(id=697)
        
        # Combinar características (X) y objetivo (y)
        X = dataset_uci.data.features
        y = dataset_uci.data.targets
        
        datos = pd.concat([X, y], axis=1)
        
        # Guardar localmente para futuros usos
        os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
        datos.to_csv(RUTA_DATOS, sep=';', index=False)
        print(f'  -> Dataset descargado y guardado en {RUTA_DATOS}')

    print(f'  -> Dataset cargado exitosamente. Dimensiones: {datos.shape}')
    return datos