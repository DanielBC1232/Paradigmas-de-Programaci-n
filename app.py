import streamlit as st
from views import upload_view, dashboard_view, interpretation_view

if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "Subir datos"

# Almacenar resultado de análisis
if "resultado_analisis" not in st.session_state:
    st.session_state.resultado_analisis = None

# Función para cambiar de página
def cambiar_pagina(pagina):
    st.session_state.pagina_actual = pagina

# Menú lateral con botones simétricos
st.sidebar.title("📊 Menú")
if st.sidebar.button("📁 Subir datos"):
    cambiar_pagina("Subir datos")
if st.sidebar.button("📈 Dashboard"):
    cambiar_pagina("Dashboard")
if st.sidebar.button("🤖 Interpretación IA"):
    cambiar_pagina("Interpretación IA")

# Renderizar vista según la página actual
pagina = st.session_state.pagina_actual

if pagina == "Subir datos":
    resultado = upload_view.render()
    if resultado:
        st.session_state.resultado_analisis = resultado
        cambiar_pagina("Interpretación IA")

elif pagina == "Dashboard":
    dashboard_view.render()

elif pagina == "Interpretación IA":
    interpretation_view.render(st.session_state.resultado_analisis)