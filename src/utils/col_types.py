import pandas as pd

# ===== Detectar tipos de columnas en un DataFrame =======================
def detectar_tipos(df):
    tipos = {
        "numericas": [],
        "categoricas": [],
        "temporales": [],
        "booleanas": []
    }

    for col in df.columns:
        p_fecha = df[col].dropna()

        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
            continue

        if es_fecha(p_fecha): # Función para detectar fechas
            tipos["temporales"].append(col)
            continue

        if pd.api.types.is_numeric_dtype(p_fecha):
            tipos["numericas"].append(col)
            continue

        tipos["categoricas"].append(col)

    return tipos

# ===== Detectar si una p_fecha es de tipo fecha ========================
def es_fecha(p_fecha):
    # Si la p_fecha está vacía, no es una fecha
    if p_fecha.empty:
        return False

    # Diferentes formatos de fecha a detectar
    formatos_fechas = [
        None,  # Auto detección de pandas
        "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y",
        "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y",
        "%d.%m.%Y", "%Y.%m.%d"
    ]

    mejor_ratio = 0
    mejor_formato = None

    # Intentar convertir la p_fecha a fecha con cada formato
    for fmt in formatos_fechas:
        fechas = pd.to_datetime(p_fecha, errors="coerce", format=fmt, dayfirst=True) # Coerce convierte errores a NaT y empieza a detectar fechas
        ratio = fechas.notnull().mean() # Proporción de fechas válidas

        # Si el % de fechas es alto, consideramos que es una fecha (80% o más)
        if ratio > mejor_ratio:
            mejor_ratio = ratio
            mejor_formato = fmt if fmt is not None else "auto" # Formato detectado
    print(mejor_formato if mejor_ratio > 0.8 else None)
    # Retorna el formato de la fecha mayoritario si es alto, de lo contrario desmiente que es una fecha
    return mejor_formato if mejor_ratio > 0.8 else None

# ===== Preparar datos numéricos para análisis ============================
def preparar_datos_numericos(df, columnas_numericas):
    for col in columnas_numericas:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df_numerico = df[columnas_numericas].dropna()

    # Retorna la lista de columnas y valores numéricos
    return df_numerico

# ===== Generar un resumen de los tipos de columnas detectados ===========
def generar_resumen_tipos(tipos):
    numericas_str = ", ".join(tipos["numericas"]) if tipos["numericas"] else "Ninguna"
    categoricas_str = ", ".join(tipos["categoricas"]) if tipos["categoricas"] else "Ninguna"

    resumen = f"Variables numéricas detectadas: {numericas_str}\n"
    resumen += f"Variables categóricas detectadas: {categoricas_str}\n"

    return resumen