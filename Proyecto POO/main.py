import streamlit as st

# Configurar la página para utilizar un layout más amplio y poner título en la pestaña
st.set_page_config(layout="wide", page_title='Análisis UNI 2016-2022', page_icon="🐼")

from resources.interfaz import mostrar_sidebar, mostrar_contenido

# Mostrar la interfaz
mostrar_sidebar()
mostrar_contenido()
