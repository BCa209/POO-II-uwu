import pandas as pd
import streamlit as st

@st.cache_data
def cargar_datos():
        file_path = 'data/matricula_uni.csv'
        return pd.read_csv(file_path, delimiter=';')