import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

def mostrar_graficos(df):

# Filtrar solo columnas numéricas (int y float)
    columnas_numericas = df.select_dtypes(include=[np.number])

    # ===== Validar si hay al menos una variable numérica para graficar =============
    if columnas_numericas.shape[1] < 1:
        st.info("No hay variables numéricas suficientes para graficar.")
        return

    # ======= Mapa de calor de correlaciones ========================================
    if columnas_numericas.shape[1] >= 2:
        st.markdown("### Mapa de correlaciones")
        fig, ax = plt.subplots(figsize=(8, 6)) # Tamaño de grafico
        # Matriz de correlación con anotaciones visuales y paleta de colores
        matriz_correlacion = columnas_numericas.corr()
        sns.heatmap(matriz_correlacion, annot=True, cmap="coolwarm", ax=ax) # Mapa de calor
        st.pyplot(fig)
    else:
        st.info("No hay suficientes variables numéricas para calcular correlaciones.")

    # ======= Detección visual de valores atípicos (outliers) =======================
    st.markdown("### Detección de valores atípicos (outliers)")
    for columna in columnas_numericas.columns:
        fig, ax = plt.subplots(figsize=(6, 2)) # Tamaño de grafico
        sns.boxplot(x=columnas_numericas[columna], ax=ax, color="skyblue") # Boxplot para detectar outliers
        ax.set_title(f"Boxplot de '{columna}'")
        st.pyplot(fig) # Render el grafico

    # ======= Visualización de relaciones fuertes entre variables ===================
    st.markdown("### Relaciones fuertes entre variables numéricas")
    correlaciones = columnas_numericas.corr()
    umbral_fuerte = 0.7  # Definimos el umbral mínimo para considerar relación fuerte

    # Extraemos la matriz triangular superior para evitar duplicados y diagonal
    matriz_superior = np.triu(np.ones(correlaciones.shape), k=1).astype(bool)
    correlaciones_filtradas = correlaciones.where(matriz_superior)

    # Convertimos la matriz filtrada a formato apilado (filas: pares de variables + valor)
    pares_correlacion = correlaciones_filtradas.stack().reset_index()
    pares_correlacion.columns = ["Variable_1", "Variable_2", "Coeficiente_de_Correlacion"]

    # Filtramos solo las relaciones con correlación fuerte (en valor absoluto)
    relaciones_fuertes = pares_correlacion[
        pares_correlacion["Coeficiente_de_Correlacion"].abs() >= umbral_fuerte
    ]

    # Visualizamos las relaciones fuertes con diagrama de dispersión
    if not relaciones_fuertes.empty:
        for _, fila in relaciones_fuertes.iterrows():
            var1, var2, corr = fila
            fig, ax = plt.subplots(figsize=(5, 4))
            sns.scatterplot(x=columnas_numericas[var1], y=columnas_numericas[var2], ax=ax)
            ax.set_title(f"{var1} vs {var2} (r = {corr:.2f})")
            st.pyplot(fig)
    else:
        st.info("No se detectaron relaciones fuertes entre variables numéricas.")