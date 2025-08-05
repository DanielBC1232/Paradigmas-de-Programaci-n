import streamlit as st
import os
from views import upload_view, dashboard_view, interpretation_view

# ====================== Configuración inicial ======================

# Pagina actual por defecto (donde se sube el csv)
if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "Subir datos"

# Resultado del analisis
if "resultado_analisis" not in st.session_state:
    st.session_state.resultado_analisis = None

# Cambiar la vista actual
def ir_a(pagina: str):
    st.session_state.pagina_actual = pagina

# ========================= Menu o barra lateral ====================

st.sidebar.title("Menú")

if st.sidebar.button("📁 Subir datos"):
    ir_a("Subir datos")

if st.sidebar.button("📈 Dashboard"):
    ir_a("Dashboard")

if st.sidebar.button("🤖 Interpretación IA"):
    ir_a("Interpretación IA")

if st.sidebar.button("🔄 Reiniciar aplicación"):
    st.session_state.clear()
    os._exit(0) #Reinicio forzado


# ========================== Vistas ================================

pagina = st.session_state.pagina_actual

if pagina == "Subir datos":
    resultado = upload_view.render()
    if resultado:
        st.session_state.resultado_analisis = resultado
        ir_a("Interpretación IA")

elif pagina == "Dashboard":
    dashboard_view.render()

elif pagina == "Interpretación IA":
    interpretation_view.render()
