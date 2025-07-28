import streamlit as st

# Esta vista recibe el diccionario con el resultado completo del análisis
def render(resultado):
    st.title("Interpretación IA")

    if not resultado:
        st.warning("Primero debes cargar o subir un archivo para analizar.")
        return

    interpretacion = resultado.get("interpretacion_ia")
    if not interpretacion:
        st.info("No se encontró ninguna interpretación de IA.")
    else:
        st.subheader("Análisis y recomendaciones")
        st.write(interpretacion)
