import pandas as pd

def detectar_tipos(df):

    # almacenar tipos de columnas
    tipos = {
        "numericas": [],
        "categoricas": [],
        "temporales": [],
        "booleanas": []
    }

    # Iterar sobre las columnas del DataFrame
    for col in df.columns:

        # Si la columna es booleana
        serie = df[col].dropna()
        # Detectar tipo boleanos
        if df[col].dtype in ["int64", "float64"]:
            tipos["numericas"].append(col)
            continue

        # Intentar convertir a fecha MM/DD/YYYY
        try:
            fecha_convertida = pd.to_datetime(serie, format="%m/%d/%Y", errors="coerce")
            if fecha_convertida.notnull().sum() / len(serie) > 0.8:
                tipos["temporales"].append(col)
                continue
        except:
            pass # No hacer nada si falla

        # Tipo numérico
        if pd.api.types.is_numeric_dtype(serie):
            tipos["numericas"].append(col)
            continue

        # Tipo Categórica
        tipos["categoricas"].append(col) 

    return tipos

def detectar_outliers(df_numerico):
    outliers = {} # almacenar variables con outliers
    for col in df_numerico.columns: # Iterar sobre cada columna numérica
        serie = df_numerico[col]    # Obtener la serie de la columna
        q1 = serie.quantile(0.25)   # Primer cuartil
        q3 = serie.quantile(0.75)   # Tercer cuartil
        iqr = q3 - q1               # Rango intercuartílico
        lower = q1 - 1.5 * iqr      # Límite inferior
        upper = q3 + 1.5 * iqr      # Límite superior
        outlier_count = ((serie < lower) | (serie > upper)).sum() # Contar outliers
        if outlier_count > 0:                                     # Si hay outliers, agregar al diccionario
            outliers[col] = outlier_count                         # Número de outliers en la columna

    # Si no hay outliers, retornar mensaje
    if not outliers:
        return "No se detectaron valores atípicos importantes."
    
    # Si hay outliers, construir mensaje
    mensaje = "Variables con valores atípicos detectados:\n"
    for col, count in outliers.items():
        mensaje += f"• {col}: {count} casos atípicos\n"
    return mensaje.strip()


def detectar_relaciones(df_numerico):

    # Verificar si hay al menos 2 columnas numéricas
    if df_numerico.shape[1] < 2:
        return None

    # Calcular la matriz de correlación
    correlacion = df_numerico.corr()
    relaciones = []

    # Iterar sobre la matriz de correlación para encontrar relaciones significativas
    for i in range(len(correlacion.columns)):
        for j in range(i+1, len(correlacion.columns)):
            var1 = correlacion.columns[i]
            var2 = correlacion.columns[j]
            r = correlacion.iloc[i, j]
            if abs(r) >= 0.75:
                relaciones.append((var1, var2, r))

    # Si no hay relaciones significativas, retornar mensaje
    if not relaciones:
        return "No se detectaron relaciones significativas entre variables."

    # Construir mensaje con las relaciones encontradas
    texto = "Relaciones significativas entre variables:\n"
    for var1, var2, r in relaciones:                    # Iterar sobre las relaciones
        texto += f"• {var1} vs {var2} → r = {r:.2f}\n"  # Formatear la relación
    return texto.strip()                                # Retornar el texto (formateado)
