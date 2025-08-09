import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe
from src.visualizer import mostrar_graficos
from AI.AI import generar_interpretacion

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("Interpretación IA")

    # Verificar si el archivo de datos existe
    if not os.path.exists(DATA_PATH):
        st.warning("Primero debes subir un archivo.")
        return

    # Cargar el DataFrame desde el archivo CSV
    df = pd.read_csv(DATA_PATH) 
    resultado = analizar_dataframe(df) # Ejecuta analyzer.py

    '''
    Ver todos los análisis realizados por el sistema y la interpretación generada por IA.
        1- Resumen del análisis
        2- Detección de tipos de variables
        3- Estadísticas descriptivas y correlación
        4- Detección de valores atípicos
        5- Información de tipos de variables
        6- Mapa de correlaciones
        7- Interpretación por IA
    '''

    # Resumen del análisis
    st.subheader("Resumen del sistema:")
    st.markdown("---") #Separador visual

    # Detección de tipos de variables
    st.subheader("Detección de tipos de variables:")
    st.text(resultado["resumen_texto"])

    st.markdown("---")

    #estadísticas descriptivas y correlación
    st.subheader("Estadísticas descriptivas:")
    st.dataframe(resultado["descriptivos"])

    st.markdown("---")

    # Detección de valores atípicos
    st.subheader("Detección de valores atípicos:")
    st.text(resultado["outliers_info"])

    st.markdown("---")

    # Información de tipos de variables
    st.subheader("Relaciones entre variables:")
    st.text(resultado["relaciones_info"])

    st.markdown("---")

    # Mapa de correlaciones
    st.subheader("Mapa de correlaciones:")
    mostrar_graficos(df)

    st.markdown("---")

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
