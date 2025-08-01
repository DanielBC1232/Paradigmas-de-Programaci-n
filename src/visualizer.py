import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

def mostrar_graficos(df):

    # Verificar si hay variables numéricas
    numericas = df.select_dtypes(include=["int64", "float64"])
    
    # Si no hay variables numericas, mostrar mensaje
    if numericas.shape[1] < 1:
        st.info("No hay variables numéricas suficientes para graficar.")
        return

    # ======= Mapa de Correlacion =======
    if numericas.shape[1] >= 2:                                             # Si hay al menos dos variables numéricas
        st.markdown("### 🔗 Mapa de correlaciones")                    
        fig, ax = plt.subplots(figsize=(8, 6))                              # Crear figura
        sns.heatmap(numericas.corr(), annot=True, cmap="coolwarm", ax=ax)   # Graficar mapa de calor de correlaciones
        st.pyplot(fig)                                                      # Mostrar gráfico
    else:
        st.info("No hay suficientes variables numéricas para calcular correlaciones.")

    # ======= Detectar outliers =======
    st.markdown("Detección de valores atípicos")
    for col in numericas.columns:                               # Graficar boxplot de cada variable numérica
        fig, ax = plt.subplots(figsize=(6, 2))                  # Crear figura
        sns.boxplot(x=numericas[col], ax=ax, color="skyblue")   # Graficar boxplot
        ax.set_title(f"Boxplot de '{col}'")                     # Título del gráfico 
        st.pyplot(fig)                                          # Mostrar gráfico

    # ======= Relaciones fuertes =======
    st.markdown("Relaciones entre variables")
    correlaciones = numericas.corr()                                    # Calcular correlaciones
    umbral = 0.7                                                        # Umbral para considerar una relación fuerte   
    relaciones = correlaciones.where(np.triu(np.ones(correlaciones.shape), k=1).astype(bool)) # Extraer relaciones fuertes
    relaciones = relaciones.stack().reset_index()                       # Convertir a DataFrame
    relaciones.columns = ["Var1", "Var2", "Correlación"]                # Renombrar columnas
    relaciones = relaciones[relaciones["Correlación"].abs() >= umbral]  # Filtrar relaciones fuertes

    # Si hay relaciones fuertes, graficarlas
    if not relaciones.empty:
        for _, row in relaciones.iterrows():         # Armar cada relación
            v1, v2, corr = row                       # Cada fila contiene dos variables y su correlación
            fig, ax = plt.subplots(figsize=(5, 4))   # Crear figura
            sns.scatterplot(x=numericas[v1], y=numericas[v2], ax=ax) # Graficar dispersión
            ax.set_title(f"{v1} vs {v2} (corr={corr:.2f})")          # Título con correlación
            st.pyplot(fig) # Mostrar gráfico
    else:
        # No hay relaciones fuertes
        st.info("No se detectaron relaciones fuertes entre variables numéricas.")
