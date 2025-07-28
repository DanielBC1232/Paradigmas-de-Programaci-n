def detectar_tipos(df):
    tipos = {"numericas": [], "categoricas": [], "temporales": [], "booleanas": []}
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
        elif df[col].dtype == "object":
            tipos["categoricas"].append(col)
        elif "date" in str(df[col].dtype).lower():
            tipos["temporales"].append(col)
        elif df[col].dropna().isin([0, 1]).all():
            tipos["booleanas"].append(col)
    return tipos
    