import itertools
import pandas as pd

# ===== Función interna para cálculo de correlaciones =====================
def obtener_relaciones(df, metodo="spearman", umbral=0.75):

    # Asegurarse de que el DataFrame tenga al menos 2 columnas numéricas
    df_num = df.select_dtypes(include="number")
    if df_num.shape[1] < 2:
        return [] # Retornar nada
    

    corr = df_num.corr(method=metodo)
    # Filtrar las relaciones que superen el umbral
    relaciones = [
        (col1, col2, corr.loc[col1, col2])
        for col1, col2 in itertools.combinations(corr.columns, 2)
        if abs(corr.loc[col1, col2]) >= umbral
    ]
    return relaciones

# ===== Detectar relaciones significativas entre variables numéricas =======
def detectar_relaciones(df, metodo="spearman", umbral=0.75):
    relaciones = obtener_relaciones(df, metodo, umbral)

    if not relaciones:
        return "No se detectaron relaciones significativas entre variables."
    
    texto = f"Relaciones {metodo.capitalize()} con |r| ≥ {umbral}:\n"
    texto += "\n".join(f"• {a} vs {b} → r = {r:.2f}" for a, b, r in relaciones)
    return texto
# ===========================================================================

# ===== Para construir el prompt de manera más limpia =======================
def correlacion_prompt(df, metodo="spearman", umbral=0.75):
    relaciones = obtener_relaciones(df, metodo, umbral)
    if not relaciones:
        return "No se detectaron correlaciones fuertes."
    return "\n".join(f"• {a} vs {b} → r = {r:.2f}" for a, b, r in relaciones)
# ===========================================================================
