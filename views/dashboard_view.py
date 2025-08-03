import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe
from src.visualizer import mostrar_graficos
from src.utils import read_csv_safe
from AI.AI import generar_interpretacion

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("Dashboard de Análisis")

    if not os.path.exists(DATA_PATH):
        st.warning("Primero debes subir un archivo.")
        return

    df = read_csv_safe(DATA_PATH) # Cargar archivo CSV
    
    # Generar graficos y análisis (PENDIENTE)
