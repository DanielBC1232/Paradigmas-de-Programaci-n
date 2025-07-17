import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def mostrar_graficos(df):
    numericas = df.select_dtypes(include=["int64", "float64"])
    if numericas.shape[1] < 2:
        st.info("No hay suficientes variables numéricas para graficar correlaciones.")
        return

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(numericas.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
