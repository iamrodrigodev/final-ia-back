import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from notebooks.src.config import DIRECTORIO_GRAFICOS, DIRECTORIO_MODELOS

def fase_4_entrenamiento_y_experimentos(X_entrenamiento, y_entrenamiento, X_prueba, y_prueba):
    print("\n=== FASE 4: ENTRENAMIENTO Y EXPERIMENTOS ===")
    
    modelos_a_evaluar = {
        "Regresion_Logistica": LogisticRegression(max_iter=1000, random_state=42),
        "Arbol_de_Decision": DecisionTreeClassifier(random_state=42),
        "Random_Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    resultados_precision = {}
    mejor_modelo = None
    mejor_precision = 0

    for nombre_modelo, modelo in modelos_a_evaluar.items():
        print(f"\n  [Experimento] Entrenando modelo: {nombre_modelo}...")
        
        puntajes_cv = cross_val_score(modelo, X_entrenamiento, y_entrenamiento, cv=5, scoring='accuracy')
        print(f"    - Precisión Validación Cruzada: {puntajes_cv.mean():.4f} (+/- {puntajes_cv.std() * 2:.4f})")
        
        modelo.fit(X_entrenamiento, y_entrenamiento)
        
        predicciones = modelo.predict(X_prueba)
        precision_prueba = accuracy_score(y_prueba, predicciones)
        resultados_precision[nombre_modelo] = precision_prueba
        print(f"    - Precisión en Prueba (Accuracy): {precision_prueba:.4f}")
        
        matriz_conf = confusion_matrix(y_prueba, predicciones)
        plt.figure(figsize=(5, 4))
        sns.heatmap(matriz_conf, annot=True, fmt="d", cmap="Blues", xticklabels=["Graduado", "Deserción"], yticklabels=["Graduado", "Deserción"])
        plt.title(f"Matriz de Confusión - {nombre_modelo}")
        plt.ylabel("Valor Real")
        plt.xlabel("Valor Predicho")
        plt.savefig(os.path.join(DIRECTORIO_GRAFICOS, f"matriz_confusion_{nombre_modelo}.png"))
        plt.close()

        if precision_prueba > mejor_precision:
            mejor_precision = precision_prueba
            mejor_modelo = modelo

    nombre_mejor_modelo = [k for k, v in resultados_precision.items() if v == mejor_precision][0]
    return resultados_precision, mejor_modelo, nombre_mejor_modelo

def fase_5_evaluacion_y_seleccion(resultados, nombre_mejor_modelo):
    print("\n=== FASE 5: EVALUACIÓN Y SELECCIÓN ===")
    print("  Resumen de Experimentos (Precisión / Accuracy):")
    for nombre, precision in resultados.items():
        print(f"    * {nombre}: {precision:.4f}")
    
    print(f"\n  >> EL MEJOR MODELO ELEGIDO ES: {nombre_mejor_modelo} con {resultados[nombre_mejor_modelo]:.4f} de precisión.")

def fase_6_guardar_salida(mejor_modelo, escalador):
    print("\n=== FASE 6: EXPORTACIÓN DEL MODELO ===")
    joblib.dump(mejor_modelo, os.path.join(DIRECTORIO_MODELOS, "modelo_desercion.pkl"))
    joblib.dump(escalador, os.path.join(DIRECTORIO_MODELOS, "escalador.pkl"))
    print("  -> Modelo y escalador guardados exitosamente en la carpeta 'models/'.")
