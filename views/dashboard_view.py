import streamlit as st
import pandas as pd
import os
from src.analyzer import analizar_dataframe
from src.visualizer import mostrar_graficos
from AI.AI import generar_interpretacion #IA

DATA_PATH = "data/uploaded_data.csv"

def render():
    st.title("📈 Dashboard de análisis")

    if not os.path.exists(DATA_PATH):
        st.warning("Primero debes subir un archivo.")
        return

    df = pd.read_csv(DATA_PATH)
    resultado = analizar_dataframe(df)

    st.subheader("Resumen del sistema:")
    st.text(resultado["resumen_texto"])

    st.subheader("Estadísticas descriptivas:")
    st.dataframe(resultado["descriptivos"])

    st.subheader("Mapa de correlaciones:")
    mostrar_graficos(df)

    st.subheader("🧠 Interpretación por IA:")
    interpretacion = generar_interpretacion(
        resultado["resumen_texto"],
        resultado["correlacion"],
        resultado["clusters"]
    )
    st.success(interpretacion)
