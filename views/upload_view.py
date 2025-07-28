import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe # Funcion de analisis del DataFrame

#Donde y como se guardan los datos:
DATA_PATH = "data/uploaded_data.csv"

# Componente streamlit para subir archivos
def render():

    # Botón para cargar CSV local
    if st.button("Cargar Datos Locales"):
        if os.path.exists(DATA_PATH):
            df = pd.read_csv(DATA_PATH)
            st.success("CSV cargado desde disco:")
            st.dataframe(df)
        else:
            st.warning("No se encontró el archivo CSV en data/archivo.csv")

    st.title("📁 Cargar archivo CSV")
    archivo = st.file_uploader("Selecciona un archivo CSV", type=["csv","xlsx"])

    # df = archivo con datos

    if archivo is not None:
        df = pd.read_csv(archivo)               # Cargar el DataFrame desde el archivo subido
        df.to_csv(DATA_PATH, index=False)
        st.success("Archivo cargado correctamente.")
        st.dataframe(df.head())
        analizar_dataframe(df)                  # Análisis del DataFrame cargado
    
    elif os.path.exists(DATA_PATH):
        st.info("Ya hay un archivo cargado:")
        df = pd.read_csv(DATA_PATH)             # Cargar el DataFrame desde el almacenamiento local
        st.dataframe(df.head())
        st.success("Archivo cargado desde el almacenamiento local.")
        analizar_dataframe(df)                  # Análisis del DataFrame cargado
    
    else:
        st.info("Por favor, sube un archivo CSV.")

