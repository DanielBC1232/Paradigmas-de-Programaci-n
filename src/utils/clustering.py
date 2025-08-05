from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Análisis de clustering para detectar grupos en datos numéricos
def analisis_clustering(df_numerico):
    if df_numerico.dropna().shape[0] >= 3:
        X = StandardScaler().fit_transform(df_numerico.dropna())
        k = min(3, X.shape[0])
        kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
        n_clusters = len(set(kmeans.labels_))
        resumen = f"Se detectaron {n_clusters} grupos por KMeans.\n"
    else:
        n_clusters = 0
        resumen = "No hay suficientes datos válidos para clustering (mínimo 3 filas).\n"

    return n_clusters, resumen
