import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from src.utils import detectar_tipos
from AI import AI

def analizar_dataframe(df):

    # Detectar tipos de columnas
    tipos = detectar_tipos(df)

    # Convertir columnas numéricas a tipo numérico
    for col in tipos["numericas"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Filtrar numéricas y quitar NaN
    df_numerico = df[tipos["numericas"]].dropna()

    resumen = f"Variables numéricas detectadas: {tipos['numericas']}\n"
    resumen += f"Variables categóricas detectadas: {tipos['categoricas']}\n"

    # Estadísticas descriptivas básicas
    descriptivos = df_numerico.describe()

    # Correlaciones
    correlacion = df_numerico.corr()

     # Clustering condicionado
    if df_numerico.shape[0] >= 3 and len(tipos["numericas"]) >= 1:
        X = StandardScaler().fit_transform(df_numerico)
        k = min(3, df_numerico.shape[0])
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        n_clusters = len(set(kmeans.labels_))
        resumen += f"\n Se detectaron {n_clusters} grupos."
    else:
        n_clusters = 0
        resumen += "\n No hay suficientes datos válidos para clustering"

    # Generar interpretación IA
    interpretacion_ia = AI.generar_interpretacion(resumen, correlacion, n_clusters)

    return {
        "tipos": tipos,
        "descriptivos": descriptivos,
        "correlacion": correlacion,
        "resumen_texto": resumen,
        "clusters": n_clusters,
        "interpretacion_ia": interpretacion_ia
    }
