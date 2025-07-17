def detectar_tipos(df):
    tipos = {"numericas": [], "categoricas": [], "fechas": []}
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
        elif df[col].dtype == "object":
            tipos["categoricas"].append(col)
        elif "date" in str(df[col].dtype).lower():
            tipos["fechas"].append(col)
    return tipos
    