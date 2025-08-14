import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe
from src.visualizer import mostrar_graficos
from AI.AI import generar_interpretacion

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("Dashboard de Análisis")

    if not os.path.exists(DATA_PATH):
        st.warning("Primero debes subir un archivo.")
        return

    df = pd.read_csv(DATA_PATH, encoding='utf-8') # Cargar archivo CSV
    resultado = analizar_dataframe(df) # Ejecuta analyzer.py

    # df = DataFrame, el archivo CSV cargado

    # Generar graficos y análisis (PENDIENTE) ==
    st.markdown("---")

    #st.subheader("Mapa de correlaciones:")
    mostrar_graficos(df)

    #st.markdown("---")
    
