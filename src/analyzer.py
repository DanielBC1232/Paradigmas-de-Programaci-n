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
    
    # Parsear de array a texto plano separado por comas
    numericas_str = ", ".join(tipos["numericas"]) if tipos["numericas"] else "Ninguna"
    categoricas_str = ", ".join(tipos["categoricas"]) if tipos["categoricas"] else "Ninguna"

    # Resumen del análisis
    resumen = f"Variables numéricas detectadas: {numericas_str}\n"
    resumen += f"Variables categóricas detectadas: {categoricas_str}\n"

    # Si no hay columnas numéricas, retornar resumen
    df_numerico = df[tipos["numericas"]].apply(pd.to_numeric, errors="coerce")

    # Estadísticas descriptivas y correlación=================================
    if df_numerico.dropna(how="all", axis=1).shape[1] == 0:
        resumen += "\nNo se encontraron columnas numéricas con datos suficientes.\n"
        descriptivos = pd.DataFrame()
        correlacion = pd.DataFrame()
    else:
        descriptivos = df_numerico.describe()
        correlacion = df_numerico.corr()

    # Clustering =============================================================
     
    if df_numerico.dropna().shape[0] >= 3:
        X = StandardScaler().fit_transform(df_numerico.dropna())
        k = min(3, X.shape[0])
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        n_clusters = len(set(kmeans.labels_))
        resumen += f"Se detectaron {n_clusters} grupos por KMeans.\n"
    else:
        n_clusters = 0
        resumen += "No hay suficientes datos válidos para clustering (mínimo 3 filas).\n"

    # Generar interpretación IA ================================================
    interpretacion_ia = AI.generar_interpretacion(resumen, correlacion, n_clusters)

    #Retornar todo el resultado
    return {
        "tipos": tipos,
        "descriptivos": descriptivos,
        "correlacion": correlacion,
        "resumen_texto": resumen,
        "clusters": n_clusters,
        "interpretacion_ia": interpretacion_ia
    }
