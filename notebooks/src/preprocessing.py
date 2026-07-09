import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def fase_3_preprocesamiento(datos: pd.DataFrame):
    print('\n=== FASE 3: PREPROCESAMIENTO ===')
    datos = datos[datos['Target'] != 'Enrolled'].copy()
    valores_nulos = datos.isnull().sum().sum()
    if valores_nulos > 0:
        datos.fillna(datos.median(numeric_only=True), inplace=True)
        print(f'  -> Se imputaron {valores_nulos} valores nulos con la mediana.')
    mapa_objetivo = {'Dropout': 1, 'Graduate': 0}
    datos['Target'] = datos['Target'].map(mapa_objetivo)
    caracteristicas = datos.drop(columns=['Target'])
    objetivo = datos['Target']
    print('  -> Balanceando clases con SMOTE (Sobremuestreo)...')
    smote = SMOTE(random_state=42)
    caracteristicas_balanceadas, objetivo_balanceado = smote.fit_resample(caracteristicas, objetivo)
    print('  -> Dividiendo datos en Entrenamiento (80%) y Prueba (20%)...')
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(caracteristicas_balanceadas, objetivo_balanceado, test_size=0.2, random_state=42)
    return (X_entrenamiento, X_prueba, y_entrenamiento, y_prueba)