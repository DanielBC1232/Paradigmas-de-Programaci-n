import pandas as pd

# Detectar tipos de columnas en un DataFrame
def detectar_tipos(df):
    tipos = {
        "numericas": [],
        "categoricas": [],
        "temporales": [],
        "booleanas": []
    }

    for col in df.columns:
        serie = df[col].dropna()

        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
            continue

        fecha_convertida = pd.to_datetime(serie, errors="coerce", dayfirst=False)
        if fecha_convertida.notnull().sum() / len(serie) > 0.8:
            tipos["temporales"].append(col)
            continue

        if pd.api.types.is_numeric_dtype(serie):
            tipos["numericas"].append(col)
            continue

        tipos["categoricas"].append(col)

    return tipos

# Preparar datos numéricos para análisis
def preparar_datos_numericos(df, columnas_numericas):
    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df_numerico = df[columnas_numericas].dropna()
    return df_numerico

# Generar un resumen de los tipos de columnas detectados
def generar_resumen_tipos(tipos):
    numericas_str = ", ".join(tipos["numericas"]) if tipos["numericas"] else "Ninguna"
    categoricas_str = ", ".join(tipos["categoricas"]) if tipos["categoricas"] else "Ninguna"

    resumen = f"Variables numéricas detectadas: {numericas_str}\n"
    resumen += f"Variables categóricas detectadas: {categoricas_str}\n"

    return resumen