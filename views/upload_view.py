import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe # Funcion de analisis del DataFrame

# Ruta donde se guarda el archivo de datos cargado
DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("📁 Cargar archivo CSV")

    # Opción para cargar datos locales ya guardados
    if st.button("Cargar Datos Locales"):
        if os.path.exists(DATA_PATH):
            try:
                df = pd.read_csv(DATA_PATH, encoding='utf-8')
                st.success("CSV cargado desde disco:")
                st.dataframe(df)
            except UnicodeDecodeError:
                st.error("El archivo está dañado o no está en UTF-8.")
        else:
            st.warning("No se encontró el archivo local")

    # Componente de subida de archivos
    archivo_subido = st.file_uploader("Selecciona un archivo CSV o Excel", type=["csv", "xlsx"])

    if archivo_subido is not None:
        # Cargar nuevo archivo subido por el usuario
        try:
            df = pd.read_csv(archivo_subido, encoding='utf-8')
            df.to_csv(DATA_PATH, index=False)  # Guardar una copia local
            st.success("Archivo cargado correctamente.")
            st.dataframe(df.head())
            analizar_dataframe(df)
        except UnicodeDecodeError:
            st.error("El archivo está dañado")
        
    elif os.path.exists(DATA_PATH):
        # Cargar archivo previamente guardado si no se sube uno nuevo
        st.info("Ya hay un archivo previamente cargado:")
        df = pd.read_csv(DATA_PATH)
        st.dataframe(df.head())
        st.success("Archivo recuperado desde el almacenamiento local.")
        analizar_dataframe(df)

    else:
        # Mensaje por defecto si no hay archivo disponible
        st.info("Por favor, sube un archivo CSV para comenzar.")
