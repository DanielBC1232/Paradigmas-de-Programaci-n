import pandas as pd

def detectar_tipos(df):
    tipos = {
        "numericas": [],
        "categoricas": [],
        "temporales": [],
        "booleanas": []
    }

    for col in df.columns:

        serie = df[col].dropna()
        # Detectar tipo boleanos
        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
            continue

        # Intentar convertir a fecha
        fecha_convertida = pd.to_datetime(serie, errors="coerce", dayfirst=False)
        if fecha_convertida.notnull().sum() / len(serie) > 0.8:
            tipos["temporales"].append(col)
            continue

        # Tipo numérico
        if pd.api.types.is_numeric_dtype(serie):
            tipos["numericas"].append(col)
            continue

        # Tipo Categórica
        tipos["categoricas"].append(col) 

    return tipos
    