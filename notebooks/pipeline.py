from notebooks.src.config import configurar_directorios
from notebooks.src.data import fase_1_obtencion_de_datos
from notebooks.src.eda import fase_2_analisis_exploratorio
from notebooks.src.preprocessing import fase_3_preprocesamiento
from notebooks.src.model import (
    fase_4_entrenamiento_y_experimentos,
    fase_5_evaluacion_y_seleccion,
    fase_6_guardar_salida
)

def ejecutar_pipeline_completo():
    """Orquestador principal que ejecuta todas las fases del pipeline de Machine Learning."""
    
    configurar_directorios()
    
    datos = fase_1_obtencion_de_datos()
    
    fase_2_analisis_exploratorio(datos)
    
    X_entrenar, X_prueba, y_entrenar, y_prueba, escalador = fase_3_preprocesamiento(datos)
    
    resultados, mejor_modelo, nombre_mejor = fase_4_entrenamiento_y_experimentos(X_entrenar, y_entrenar, X_prueba, y_prueba)
    
    fase_5_evaluacion_y_seleccion(resultados, nombre_mejor)
    
    fase_6_guardar_salida(mejor_modelo, escalador)
    
    print("\n¡Pipeline ejecutado al 100% de forma modular!")

if __name__ == "__main__":
    ejecutar_pipeline_completo()
