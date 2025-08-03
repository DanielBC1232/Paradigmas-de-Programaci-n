import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe
from src.visualizer import mostrar_graficos
from src.utils import read_csv_safe
from AI.AI import generar_interpretacion

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("Interpretación IA")

    # Verificar si el archivo de datos existe
    if not os.path.exists(DATA_PATH):
        st.warning("Primero debes subir un archivo.")
        return

    df = read_csv_safe(DATA_PATH) # Cargar el DataFrame desde el archivo CSV
    resultado = analizar_dataframe(df)

    # Resumen del análisis
    st.subheader("Resumen del sistema:")
    st.text(resultado["resumen_texto"])

    #estadísticas descriptivas y correlación
    st.subheader("Estadísticas descriptivas:")
    st.dataframe(resultado["descriptivos"])

    # Detección de valores atípicos
    st.subheader("Detección de valores atípicos:")
    st.text(resultado["outliers_info"])

    # Información de tipos de variables
    st.subheader("Relaciones entre variables:")
    st.text(resultado["relaciones_info"])

    # Mapa de correlaciones
    st.subheader("Mapa de correlaciones:")
    mostrar_graficos(df)

    # Interpretación por IA
    st.subheader("Interpretación por IA:")
    interpretacion = generar_interpretacion(
        resumen=resultado["resumen_texto"],
        correlacion=resultado["correlacion"],
        n_clusters=resultado["clusters"],
        outliers_info=resultado["outliers_info"],
        relaciones_info=resultado["relaciones_info"]
    )
    st.success(interpretacion)
