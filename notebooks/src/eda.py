import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from notebooks.src.config import DIRECTORIO_GRAFICOS

def fase_2_analisis_exploratorio(datos: pd.DataFrame):
    print("\n=== FASE 2: ANÁLISIS EXPLORATORIO (EDA) ===")
    
    plt.figure(figsize=(8, 5))
    sns.countplot(data=datos, x="Target", palette="viridis")
    plt.title("Distribución de Clases (Objetivo)")
    plt.savefig(os.path.join(DIRECTORIO_GRAFICOS, "distribucion_clases.png"))
    plt.close()
    print("  -> Gráfico de distribución de clases guardado.")

    columnas_numericas = datos.select_dtypes(include=[np.number]).columns.tolist()
    plt.figure(figsize=(12, 10))
    sns.heatmap(datos[columnas_numericas[:10]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de Correlación (Top 10 variables numéricas)")
    plt.savefig(os.path.join(DIRECTORIO_GRAFICOS, "matriz_correlacion.png"))
    plt.close()
    print("  -> Matriz de correlación guardada.")
