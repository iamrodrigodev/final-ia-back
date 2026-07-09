import os
DIRECTORIO_BASE = os.path.dirname(os.path.dirname(__file__))
DIRECTORIO_GRAFICOS = os.path.join(DIRECTORIO_BASE, '../data/plots')
DIRECTORIO_MODELOS = os.path.join(DIRECTORIO_BASE, '../models')
DIRECTORIO_RESULTADOS = os.path.join(DIRECTORIO_BASE, '../data/results')
RUTA_DATOS = os.path.join(DIRECTORIO_BASE, '../data/raw/data.csv')

def configurar_directorios():
    print('--- Configurando directorios ---')
    os.makedirs(DIRECTORIO_GRAFICOS, exist_ok=True)
    os.makedirs(DIRECTORIO_MODELOS, exist_ok=True)
    os.makedirs(DIRECTORIO_RESULTADOS, exist_ok=True)
