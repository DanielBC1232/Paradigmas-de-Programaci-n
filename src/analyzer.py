import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from src.utils import detectar_tipos, detectar_outliers, detectar_relaciones
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

    # Resumen inicial
    resumen = f"Variables numéricas detectadas: {numericas_str}\n"
    resumen += f"Variables categóricas detectadas: {categoricas_str}\n"

    # Estadísticas descriptivas y correlación
    df_numerico = df[tipos["numericas"]].apply(pd.to_numeric, errors="coerce")

    # Si no hay columnas numéricas con datos suficientes
    if df_numerico.dropna(how="all", axis=1).shape[1] == 0:
        resumen += "\nNo se encontraron columnas numéricas con datos suficientes.\n"
        descriptivos = pd.DataFrame()
        correlacion = pd.DataFrame()
        outliers_info = "No se pudo analizar valores atípicos por falta de datos.\n"
        relaciones_info = "No hay suficientes variables para analizar relaciones.\n"
    else:
        # Estadísticas
        descriptivos = df_numerico.describe()
        correlacion = df_numerico.corr()

    # ===== Outliers & Relaciones Bivariadas
    outliers_info = detectar_outliers(df_numerico)
    relaciones_info = detectar_relaciones(df_numerico)

    # CLUSTERING =============================================================
    df_for_clustering = df_numerico.dropna()
    if df_for_clustering.shape[0] >= 3 and df_for_clustering.shape[1] > 0:
        X = StandardScaler().fit_transform(df_for_clustering)        # Normalizar datos
        k = min(3, X.shape[0])                                       # Usar 3 clusters como máximo si hay suficientes datos
        if k > 0:  # Verificar que k sea válido
            kmeans = KMeans(n_clusters=k, random_state=0).fit(X)     # Aplicar KMeans
            n_clusters = len(set(kmeans.labels_))                    # Número de clusters detectados 
            resumen += f"Se detectaron {n_clusters} grupos por KMeans.\n"   # Resumen de clusters
        else:
            n_clusters = 0
            resumen += "No hay suficientes datos válidos para clustering.\n"
    else:
        # Si no hay suficientes datos
        n_clusters = 0
        resumen += "No hay suficientes datos válidos para clustering (mínimo 3 filas).\n"

    # INTERPRETACIÓN IA ======================================================
    interpretacion_ia = AI.generar_interpretacion(
        resumen,
        correlacion,
        n_clusters,
        outliers_info,
        relaciones_info
    )

    return {
        "tipos": tipos,
        "descriptivos": descriptivos,
        "correlacion": correlacion,
        "resumen_texto": resumen,
        "clusters": n_clusters,
        "outliers_info": outliers_info,
        "relaciones_info": relaciones_info,
        "interpretacion_ia": interpretacion_ia
    }
