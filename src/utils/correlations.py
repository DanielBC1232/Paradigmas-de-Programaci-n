import itertools

# ===== Detectar relaciones significativas entre variables numéricas =======
def detectar_relaciones(df_numerico, umbral=0.75):
    if df_numerico.shape[1] < 2:
        return "No hay suficientes variables numéricas para analizar relaciones."

    correlacion = df_numerico.corr()
    relaciones = []

    for i, col1 in enumerate(correlacion.columns):
        for j in range(i + 1, len(correlacion.columns)):
            col2 = correlacion.columns[j]
            r = correlacion.iloc[i, j]
            if abs(r) >= umbral:
                relaciones.append((col1, col2, r))

    if not relaciones:
        return "No se detectaron relaciones significativas entre variables."

    texto = "Relaciones significativas entre variables:\n"
    texto += "\n".join(f"• {a} vs {b} → r = {r:.2f}" for a, b, r in relaciones) # Formatear a dos decimales
    return texto # Retornar el texto (formateado)
# ===========================================================================

# ===== Para contruir el prompt de manera más limpia=========================
def correlacion_prompt(correlacion, umbral=0.75):
    texto_corr = ""
    for fila, col in itertools.combinations(correlacion.columns, 2):
        r = correlacion.loc[fila, col]
        if abs(r) >= umbral:
            texto_corr += f"• {fila} vs {col} → r = {r:.2f}\n"
    return texto_corr or "No se detectaron correlaciones fuertes."
# ============================================================================