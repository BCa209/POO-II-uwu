import streamlit as st

def mostrar_presentacion():
    st.title("Analisis de los Datos de Estudiantes Matriculados a La Universidad Nacional de Ingeneria (2016-2022) para Programación Orientada a Objetos II")
    st.image('images/EPIS_UNAP.png', caption='Escuela Profesional de Ingenieria de Sistemas', width=500)

# Función para la portada
def mostrar_portada():
    st.header("Bienvenido al Dashboard de Análisis de Postulantes")
    st.write("""
    Esta página proporciona un análisis detallado de los matriculados a diferentes carreras universitarias
    de la Univer    sidad Nacional de Ingeniería durante los años 2016 al 2022.
    Utilice los botones debajo para navegar por las diferentes secciones del análisis.
    """)
    st.subheader("Contenido")
    st.write("Facultades")
    st.write("Distribucion de Hecho")
    st.write("Distribucion de Edades")
    st.write("Distribucion por Genero")
    st.write("Distribuciion por Facultad")
    st.write("Distribuciion por Nacionalidad")
    st.write("Distribuciion por Residencia por Distrito")
    st.write("Distribuciion por Residencia por Provincia")
    st.write("Distribuciion por Residencia por Departamento")
    st.write("Distribuciion por Modalidad")
    st.write("Distribuciion por Metologia")
    st.write("Distribuciion por Especialidad")
    st.write("Distribuciion por Ciclo Relativo")