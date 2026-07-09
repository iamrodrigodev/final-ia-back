import os
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from notebooks.src.config import DIRECTORIO_GRAFICOS, DIRECTORIO_MODELOS

def fase_4_entrenamiento_y_experimentos(X_entrenamiento, y_entrenamiento, X_prueba, y_prueba):
    print('\n=== FASE 4: ENTRENAMIENTO AVANZADO Y TUNING (GridSearchCV) ===')
    
    # Definición de Pipelines base
    pipe_lr = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif)),
        ('classifier', LogisticRegression(random_state=42, max_iter=2000))
    ])
    
    pipe_rf = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif)),
        ('classifier', RandomForestClassifier(random_state=42))
    ])
    
    # Grillas de Hiperparámetros
    param_grid_lr = {
        'selector__k': [10, 15, 'all'],
        'classifier__C': [0.1, 1.0, 10.0]
    }
    
    param_grid_rf = {
        'selector__k': [10, 15, 'all'],
        'classifier__n_estimators': [50, 100],
        'classifier__max_depth': [None, 10, 20]
    }
    
    grids = {
        'Regresion_Logistica': GridSearchCV(pipe_lr, param_grid_lr, cv=5, scoring='f1', n_jobs=-1),
        'Random_Forest': GridSearchCV(pipe_rf, param_grid_rf, cv=5, scoring='f1', n_jobs=-1)
    }
    
    resultados_f1 = {}
    mejor_modelo = None
    mejor_f1 = 0
    nombre_mejor_modelo = ""
    
    for nombre_modelo, grid in grids.items():
        print(f'\n  [GridSearchCV] Optimizando hiperparámetros para: {nombre_modelo}...')
        grid.fit(X_entrenamiento, y_entrenamiento)
        
        modelo_optimizado = grid.best_estimator_
        print(f'    - Mejores parámetros: {grid.best_params_}')
        
        predicciones = modelo_optimizado.predict(X_prueba)
        predicciones_proba = modelo_optimizado.predict_proba(X_prueba)[:, 1]
        
        # Calcular múltiples métricas
        roc_auc = roc_auc_score(y_prueba, predicciones_proba)
        
        print(f'    - Reporte de Clasificación en Prueba:\n{classification_report(y_prueba, predicciones)}')
        print(f'    - ROC-AUC: {roc_auc:.4f}')
        
        # Guardaremos el modelo en base a su score del Grid (F1 validacion cruzada)
        score_cv = grid.best_score_
        resultados_f1[nombre_modelo] = score_cv
        
        matriz_conf = confusion_matrix(y_prueba, predicciones)
        plt.figure(figsize=(5, 4))
        sns.heatmap(matriz_conf, annot=True, fmt='d', cmap='Blues', xticklabels=['Graduado', 'Deserción'], yticklabels=['Graduado', 'Deserción'])
        plt.title(f'Matriz Confusión (Optimizada) - {nombre_modelo}')
        plt.ylabel('Valor Real')
        plt.xlabel('Valor Predicho')
        plt.savefig(os.path.join(DIRECTORIO_GRAFICOS, f'matriz_confusion_{nombre_modelo}.png'))
        plt.close()
        
        if score_cv > mejor_f1:
            mejor_f1 = score_cv
            mejor_modelo = modelo_optimizado
            nombre_mejor_modelo = nombre_modelo
            
    return (resultados_f1, mejor_modelo, nombre_mejor_modelo)

def fase_5_evaluacion_y_seleccion(resultados, nombre_mejor_modelo):
    print('\n=== FASE 5: EVALUACIÓN Y SELECCIÓN ===')
    print('  Resumen de Experimentos (F1-Score en Validación Cruzada):')
    for nombre, score in resultados.items():
        print(f'    * {nombre}: {score:.4f}')
    print(f'\n  >> EL MEJOR MODELO ELEGIDO ES: {nombre_mejor_modelo} con {resultados[nombre_mejor_modelo]:.4f} de F1-Score.')

def fase_6_guardar_salida(mejor_pipeline):
    print('\n=== FASE 6: EXPORTACIÓN DEL MODELO ===')
    # Guardamos todo el pipeline en un solo archivo
    joblib.dump(mejor_pipeline, os.path.join(DIRECTORIO_MODELOS, 'pipeline_desercion.pkl'))
    print("  -> Pipeline completo (Escalador + Selector + Clasificador) guardado como 'pipeline_desercion.pkl'.")