import streamlit as st
from views import upload_view, dashboard_view

if "pagina_actual" not in st.session_state:
    st.session_state.pagina_actual = "Subir datos"

def cambiar_pagina(pagina):
    st.session_state.pagina_actual = pagina

st.sidebar.title("📊 Menú")
if st.sidebar.button("📁 Subir datos"):
    cambiar_pagina("Subir datos")
if st.sidebar.button("📈 Dashboard"):
    cambiar_pagina("Dashboard")

pagina = st.session_state.pagina_actual

if pagina == "Subir datos":
    upload_view.render()
elif pagina == "Dashboard":
    dashboard_view.render()
