import streamlit as st
import pandas as pd
import os

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("📁 Cargar archivo CSV")
    archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv","xlsx"])

    if archivo is not None:
        df = pd.read_csv(archivo)
        df.to_csv(DATA_PATH, index=False)
        st.success("Archivo cargado correctamente.")
        st.dataframe(df.head())
    elif os.path.exists(DATA_PATH):
        st.info("Ya hay un archivo cargado:")
        df = pd.read_csv(DATA_PATH)
        st.dataframe(df.head())
    else:
        st.info("Por favor, sube un archivo CSV.")
