import os

import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from notebooks.src.config import DIRECTORIO_GRAFICOS, DIRECTORIO_MODELOS, DIRECTORIO_RESULTADOS


def fase_4_entrenamiento_y_experimentos(X_entrenamiento, y_entrenamiento, X_prueba, y_prueba):
    print('\n=== FASE 4: ENTRENAMIENTO AVANZADO Y TUNING (GridSearchCV) ===')

    pipe_lr = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif)),
        ('classifier', LogisticRegression(random_state=42, max_iter=2000)),
    ])

    pipe_dt = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif)),
        ('classifier', DecisionTreeClassifier(random_state=42)),
    ])

    pipe_rf = Pipeline([
        ('scaler', StandardScaler()),
        ('selector', SelectKBest(score_func=f_classif)),
        ('classifier', RandomForestClassifier(random_state=42)),
    ])

    grids = {
        'Regresion_Logistica': GridSearchCV(
            pipe_lr,
            {
                'selector__k': [10, 15, 'all'],
                'classifier__C': [0.1, 1.0, 10.0],
            },
            cv=5,
            scoring='f1',
            n_jobs=-1,
        ),
        'Arbol_de_Decision': GridSearchCV(
            pipe_dt,
            {
                'selector__k': [10, 15, 'all'],
                'classifier__max_depth': [None, 5, 10],
                'classifier__min_samples_split': [2, 10],
            },
            cv=5,
            scoring='f1',
            n_jobs=-1,
        ),
        'Random_Forest': GridSearchCV(
            pipe_rf,
            {
                'selector__k': [10, 15, 'all'],
                'classifier__n_estimators': [50, 100],
                'classifier__max_depth': [None, 10, 20],
            },
            cv=5,
            scoring='f1',
            n_jobs=-1,
        ),
    }

    resultados_f1 = {}
    filas_resultados = []
    mejor_modelo = None
    mejor_f1 = 0
    nombre_mejor_modelo = ''

    for nombre_modelo, grid in grids.items():
        print(f'\n  [GridSearchCV] Optimizando hiperparametros para: {nombre_modelo}...')
        grid.fit(X_entrenamiento, y_entrenamiento)

        modelo_optimizado = grid.best_estimator_
        print(f'    - Mejores parametros: {grid.best_params_}')

        predicciones = modelo_optimizado.predict(X_prueba)
        predicciones_proba = modelo_optimizado.predict_proba(X_prueba)[:, 1]

        score_cv = grid.best_score_
        accuracy = accuracy_score(y_prueba, predicciones)
        precision = precision_score(y_prueba, predicciones, zero_division=0)
        recall = recall_score(y_prueba, predicciones, zero_division=0)
        f1_prueba = f1_score(y_prueba, predicciones, zero_division=0)
        roc_auc = roc_auc_score(y_prueba, predicciones_proba)

        print(f'    - Reporte de Clasificacion en Prueba:\n{classification_report(y_prueba, predicciones)}')
        print(f'    - ROC-AUC: {roc_auc:.4f}')

        resultados_f1[nombre_modelo] = score_cv
        filas_resultados.append({
            'modelo': nombre_modelo,
            'mejor_f1_cv': score_cv,
            'accuracy_prueba': accuracy,
            'precision_prueba': precision,
            'recall_prueba': recall,
            'f1_prueba': f1_prueba,
            'roc_auc_prueba': roc_auc,
            'mejores_parametros': grid.best_params_,
        })

        matriz_conf = confusion_matrix(y_prueba, predicciones)
        plt.figure(figsize=(5, 4))
        sns.heatmap(
            matriz_conf,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=['Graduado', 'Desercion'],
            yticklabels=['Graduado', 'Desercion'],
        )
        plt.title(f'Matriz Confusion (Optimizada) - {nombre_modelo}')
        plt.ylabel('Valor Real')
        plt.xlabel('Valor Predicho')
        plt.savefig(os.path.join(DIRECTORIO_GRAFICOS, f'matriz_confusion_{nombre_modelo}.png'))
        plt.close()

        if score_cv > mejor_f1:
            mejor_f1 = score_cv
            mejor_modelo = modelo_optimizado
            nombre_mejor_modelo = nombre_modelo

    ruta_resultados = os.path.join(DIRECTORIO_RESULTADOS, 'resultados_experimentos.csv')
    pd.DataFrame(filas_resultados).to_csv(ruta_resultados, index=False)
    print(f'\n  -> Resultados comparativos guardados en {ruta_resultados}')

    return resultados_f1, mejor_modelo, nombre_mejor_modelo


def fase_5_evaluacion_y_seleccion(resultados, nombre_mejor_modelo):
    print('\n=== FASE 5: EVALUACION Y SELECCION ===')
    print('  Resumen de Experimentos (F1-Score en Validacion Cruzada):')
    for nombre, score in resultados.items():
        print(f'    * {nombre}: {score:.4f}')
    print(f'\n  >> EL MEJOR MODELO ELEGIDO ES: {nombre_mejor_modelo} con {resultados[nombre_mejor_modelo]:.4f} de F1-Score.')


def fase_6_guardar_salida(mejor_pipeline):
    print('\n=== FASE 6: EXPORTACION DEL MODELO ===')
    joblib.dump(mejor_pipeline, os.path.join(DIRECTORIO_MODELOS, 'pipeline_desercion.pkl'))
    print("  -> Pipeline completo (Escalador + Selector + Clasificador) guardado como 'pipeline_desercion.pkl'.")
