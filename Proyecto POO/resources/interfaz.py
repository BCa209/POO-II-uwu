import streamlit as st
from resources.cargar_datos import cargar_datos
from resources.analisis import filtrar_por_anios
from resources.graficos import mostrar_datos_anio, mostrar_analisis_periodo, mostrar_analisis_tipo_de_hecho, mostrar_analisis_genero, mostrar_analisis_nacionalidad, mostrar_analisis_anio_nacimiento, mostrar_analisis_edad, mostrar_analisis_departamento_colegio, mostrar_analisis_distrito_residencia, mostrar_analisis_provincia_residencia, mostrar_analisis_departamento_residencia, mostrar_analisis_modalidad, mostrar_analisis_metodologia, mostrar_analisis_facultad, mostrar_analisis_especialidad, mostrar_analisis_ciclo_relativo

from resources.mostrar_images import mostrar_logo_uni1, mostrar_logo_uni, mostrar_images_facultades
from resources.portada import mostrar_portada, mostrar_presentacion

# Cargar los datos
df = cargar_datos()

# Inicializar el estado de la aplicación
if 'pagina_actual' not in st.session_state:
    st.session_state.pagina_actual = 'portada'

# Crear el layout de la interfaz
def mostrar_sidebar():
    #------Barra lateral------#
    #mostrar_logo_uni()
    st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/f/f7/Uni-logo_transparente_granate.png',caption='UNIVERSIDAD NACIONAL DE INGENIERIA', use_column_width=True, output_format="JPEG")
    st.sidebar.title("Panel de Navegación")

    if 'pagina_actual' not in st.session_state:
        st.session_state.pagina_actual = 'presentacion'
    # Botones
    if st.sidebar.button("Inicio"):
        st.session_state.pagina_actual = 'portada'

    if st.sidebar.button("Facultades"):
        st.session_state.pagina_actual = 'enum_facultades'
    if st.sidebar.button("Distribución de Hecho"):
        st.session_state.pagina_actual = 'hecho'
    if st.sidebar.button("Distribución de Edades"):
        st.session_state.pagina_actual = 'edades'
    if st.sidebar.button("Distribución por Género"):
        st.session_state.pagina_actual = 'genero'
    if st.sidebar.button("Distribución por Facultad"):
        st.session_state.pagina_actual = 'facultad'
    if st.sidebar.button("Distribución por Nacionalidad"):
        st.session_state.pagina_actual = 'nacionalidad'
    if st.sidebar.button("Distribución por Residencia por distrito"):
        st.session_state.pagina_actual = 'residencia_distrito'
    if st.sidebar.button("Distribución por Residencia por provincia"):
        st.session_state.pagina_actual = 'residencia_provincia'
    if st.sidebar.button("Distribución por Residencia por departamento"):
        st.session_state.pagina_actual = 'residencia_departamento'
    if st.sidebar.button("Distribución por Modalidad"):
        st.session_state.pagina_actual = 'modalidad'
    if st.sidebar.button("Distribución por Metodología"):
        st.session_state.pagina_actual = 'metodologia'
    if st.sidebar.button("Distribución por Especialidad"):
        st.session_state.pagina_actual = 'especialidad'
    if st.sidebar.button("Distribución por Ciclo Relativo"):
        st.session_state.pagina_actual = 'ciclo_relativo'

def mostrar_contenido():
    if st.session_state.pagina_actual == 'presentacion':
        mostrar_presentacion()
    #-------Mostrar el contenido según el estado de la aplicacion------#
    if st.session_state.pagina_actual == 'portada':
        mostrar_portada()
    if st.session_state.pagina_actual == 'enum_facultades':
        st.title('FACULTADES DE LA UNIVERSIDAD NACIONAL DE INGENIERIA')
        mostrar_images_facultades()

    if st.session_state.pagina_actual == 'hecho':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_tipo_de_hecho(df_filtrado)

    if st.session_state.pagina_actual == 'edades':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_edad(df_filtrado)
    
    if st.session_state.pagina_actual == 'genero':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_genero(df_filtrado)
    
    if st.session_state.pagina_actual == 'facultad':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_facultad(df_filtrado)
    
    if st.session_state.pagina_actual == 'nacionalidad':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_nacionalidad(df_filtrado)
    
    if st.session_state.pagina_actual == 'residencia_distrito':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_distrito_residencia(df_filtrado)
    
    if st.session_state.pagina_actual == 'residencia_provincia':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_provincia_residencia(df_filtrado)
    
    if st.session_state.pagina_actual == 'residencia_departamento':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_departamento_residencia(df_filtrado)
    
    if st.session_state.pagina_actual == 'modalidad':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_modalidad(df_filtrado)
    
    if st.session_state.pagina_actual == 'metodologia':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_metodologia(df_filtrado)
    
    if st.session_state.pagina_actual == 'especialidad':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_especialidad(df_filtrado)
    
    if st.session_state.pagina_actual == 'ciclo_relativo':
        anios = st.multiselect('Selecciona el/los años de matrícula(2016-2022)', options=df['matricula'].unique(), default=df['matricula'].unique())
        df_filtrado = filtrar_por_anios(df, anios)
        mostrar_analisis_ciclo_relativo(df_filtrado)
