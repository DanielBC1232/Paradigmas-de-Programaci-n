import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from AI import AI
from src.utils.correlations import detectar_relaciones
from src.utils.outliers import detectar_outliers
from src.utils.col_types import detectar_tipos, preparar_datos_numericos, generar_resumen_tipos
from src.utils.clustering import analisis_clustering

# Función para analizar el DataFrame que se le pasa por parámetro
def analizar_dataframe(df):
    
    resumen = ""

    # ===== Verificar tipos =======================================================
    tipos = detectar_tipos(df)
    # =============================================================================

    # ===== Resumen de tipos ======================================================
    df_numerico = preparar_datos_numericos(df, tipos["numericas"])
    # =============================================================================

    # ===== Descriptivos y correlación ============================================
    if df_numerico.dropna(how="all", axis=1).shape[1] == 0:
        descriptivos = pd.DataFrame()
        correlacion = pd.DataFrame()
        resumen += "\nNo se encontraron columnas numéricas con datos suficientes.\n"
    else:
        descriptivos = df_numerico.describe()
        correlacion = df_numerico.corr()
    # =============================================================================


    # ===== Resumen descriptivo ===================================================
    resumen = generar_resumen_tipos(tipos)
    #==============================================================================
    
    # ===== Outliers & Relaciones Bivariadas ======================================
    outliers_info = detectar_outliers(df_numerico)
    # =============================================================================

    # ===== Relaciones Bivariadas =================================================
    relaciones_info = detectar_relaciones(df_numerico)
    # =============================================================================

    # ===== Análisis de clustering =================================================
    n_clusters, resumen_clusters = analisis_clustering(df_numerico)
    resumen += resumen_clusters # Agregar resumen de clustering al texto
    # =============================================================================

    # INICIO INTERPRETACIÓN IA ======================================================
    interpretacion_ia = AI.generar_interpretacion(
        resumen,
        correlacion,
        n_clusters,
        outliers_info,
        relaciones_info
    )
    # FIN INTERPRETACIÓN IA ======================================================

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
