
# Detectar y manejar outliers
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