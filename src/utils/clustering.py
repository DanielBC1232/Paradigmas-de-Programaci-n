from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Means es un algoritmo de clustering que agrupa datos en K grupos basados en la distancia entre ellos.
# K = número de clusters o grupos a detectar
# X = datos a agrupar, en este caso, las columnas numéricas del DataFrame

# Análisis de clustering para detectar grupos en datos numéricos
def analisis_clustering(df_numerico):

    # Verificar si hay suficientes datos para clustering (3 o mas filas de clustering, no de dataframe)
    if df_numerico.dropna().shape[0] >= 3:
 
        # ===== Aplicar KMeans =======================================================
        scaler = StandardScaler()
        X = scaler.fit_transform(df_numerico.dropna())                  # Normalizar las columnas numéricas
        k = min(3, X.shape[0])                                          # Determinar el número de clusters (mínimo 3 o menos si hay menos filas)
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=10).fit(X) # Ajustar KMeans
        n_clusters = len(set(kmeans.labels_))                           # Número de clusters detectados         
        resumen = f"Se detectaron {n_clusters} grupos por KMeans.\n"    # Resumen del análisis (Para mostrar al usuario y analizar más tarde en IA)

        # ===== Calcular centroides y tamaño de cada cluster =========================
        centroides = pd.DataFrame(
            scaler.inverse_transform(kmeans.cluster_centers_),
            columns=df_numerico.columns
        )

        # ===== Agregar descripción de clusters al resumen ============================
        for i, fila in centroides.iterrows():
            resumen += f"Cluster {i}: "
            resumen += ", ".join([f"{col} ≈ {fila[col]:.2f}" for col in df_numerico.columns])
            resumen += "\n"
        
    else:
        # Si hay pocas filas, no se puede hacer clustering (menos de 3 filas clustering)
        n_clusters = 0
        resumen = "No hay suficientes datos válidos para clustering (mínimo 3 filas).\n"

    return n_clusters, resumen
