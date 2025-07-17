import numpy as np
from scipy import stats
from sklearn.cluster import KMeans
from src.utils import detectar_tipos

def analizar_dataframe(df):
    tipos = detectar_tipos(df)
    numericas = df.select_dtypes(include=["int64", "float64"])

    descriptivos = numericas.describe()

    z_scores = np.abs(stats.zscore(numericas))
    outliers = (z_scores > 3).sum().sum()
    porc_outliers = 100 * outliers / len(df)

    modelo = KMeans(n_clusters=3, n_init=10, random_state=0)
    etiquetas = modelo.fit_predict(numericas)

    resumen = f"Variables numéricas detectadas: {tipos['numericas']}\n"
    resumen += f"Se detectaron {porc_outliers:.2f}% de outliers (Z-score > 3).\n"
    resumen += f"Se identificaron 3 clusters con KMeans."

    return {
        "resumen_texto": resumen,
        "descriptivos": descriptivos,
        "correlacion": numericas.corr(),
        "clusters": etiquetas,
        "porcentaje_outliers": porc_outliers
    }
