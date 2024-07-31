import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from resources.analisis import (analisis_periodo, analisis_tipo_de_hecho, analisis_genero, analisis_nacionalidad, 
                    analisis_anio_nacimiento, analisis_edad, analisis_departamento_colegio, 
                    analisis_distrito_residencia, analisis_provincia_residencia, 
                    analisis_departamento_residencia, analisis_modalidad, 
                    analisis_metodologia, analisis_facultad, analisis_especialidad, 
                    analisis_ciclo_relativo)

def mostrar_datos_anio(df_filtrado, anios):
    st.write(f'Datos filtrados para los años: {anios}')
    st.dataframe(df_filtrado)

# Definición de los países con sus códigos
nacionalidades_codigos = {
    'Alemania': 'DEU',
    'Argentina': 'ARG',
    'Bolivia': 'BOL',
    'Brasil': 'BRA',
    'Chile': 'CHL',
    'China': 'CHN',
    'Colombia': 'COL',
    'Corea Republica': 'KOR',
    'España': 'ESP',
    'Estados Unidos': 'USA',
    'Francia': 'FRA',
    'Guatemala': 'GTM',
    'Italia': 'ITA',
    'Japon': 'JPN',
    'Mexico': 'MEX',
    'Nueva Zelandia': 'NZL',
    'Paraguay': 'PRY',
    'Perú': 'PER',
    'RSS de Ucrania': 'UKR',
    'Rusia': 'RUS',
    'Suiza': 'CHE',
    'Venezuela': 'VEN'
}

# Analisis por Periodo
def mostrar_analisis_periodo(df_filtrado):
    st.subheader('Distribución de Periodo')
    periodo_stats = analisis_periodo(df_filtrado)
    st.write(periodo_stats)
    periodo_counts = analisis_periodo(df_filtrado)
    st.bar_chart(periodo_counts)

# Analisis tipo de Hecho
def mostrar_analisis_tipo_de_hecho(df_filtrado):
    st.subheader('Distribución de Tipos de Hecho')
    thecho_stats = analisis_tipo_de_hecho(df_filtrado)
    st.write(thecho_stats)
    
    tipo_de_hecho_counts = analisis_tipo_de_hecho(df_filtrado)
    fig_tipo_de_hecho = px.pie(values=tipo_de_hecho_counts.values, names=tipo_de_hecho_counts.index, title='Distribución de Tipos de Hecho')
    st.plotly_chart(fig_tipo_de_hecho)

# Analisis de Genero
def mostrar_analisis_genero(df_filtrado):
    st.subheader('Distribución de Género')
    genero_stats = analisis_genero(df_filtrado)
    st.write(genero_stats)
    
    genero_counts = analisis_genero(df_filtrado)
    colors = ['lightgreen', 'darkorange']
    labels=genero_counts.index
    values=genero_counts.values
    fig_genero = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
    fig_genero.update_traces(
        hoverinfo='label+percent', 
        textinfo='value', 
        textfont_size=20, 
        marker=dict(colors=colors, line=dict(color='black', width=3))
    )
    st.plotly_chart(fig_genero)

# Analisis de Nacionalidad
def mostrar_analisis_nacionalidad(df_filtrado):
    st.subheader('Distribución de Nacionalidad')
    nacionalidad_stats = analisis_nacionalidad(df_filtrado)
    st.write(nacionalidad_stats)
    nacionalidad_counts = analisis_nacionalidad(df_filtrado).reset_index()
    nacionalidad_counts.columns = ['Nacionalidad', 'count']
    fig_nacionalidad = px.choropleth(
        nacionalidad_counts,
        locations='Nacionalidad',
        locationmode='country names',
        color='count',
        hover_name='Nacionalidad',
        color_continuous_scale=px.colors.sequential.Plasma,
        title='Distribución de Nacionalidad'
    )
    st.plotly_chart(fig_nacionalidad)

# Analisis de año de Nacimiento
def mostrar_analisis_anio_nacimiento(df_filtrado):
    st.subheader('Distribución de Año de Nacimiento')
    nacimiento_stats = analisis_anio_nacimiento(df_filtrado)
    st.write(nacimiento_stats)
    anio_nacimiento_counts = analisis_anio_nacimiento(df_filtrado)
    fig_ano_nacimiento = px.histogram(df_filtrado, x='Nacimiento', nbins=20, title='Distribución de Año de Nacimiento')
    st.plotly_chart(fig_ano_nacimiento)

# Analisis de Edad
def mostrar_analisis_edad(df_filtrado):
    st.subheader('Análisis de Edad')
    edad_stats = analisis_edad(df_filtrado)
    st.write(edad_stats)
    fig_edad = px.histogram(df_filtrado, x='Edad', nbins=20, title='Distribución de Edad')
    st.plotly_chart(fig_edad)

# Departamento de Coledio
def mostrar_analisis_departamento_colegio(df_filtrado):
    st.subheader('Distribución por Departamento de Colegio')
    depcolegio_stats = analisis_departamento_colegio(df_filtrado)
    st.write(depcolegio_stats)
    departamento_colegio_counts = analisis_departamento_colegio(df_filtrado)
    fig_departamento_colegio = px.bar(departamento_colegio_counts, x=departamento_colegio_counts.index, y=departamento_colegio_counts.values, title='Distribución por Departamento de Colegio')
    st.plotly_chart(fig_departamento_colegio)

# Analisis de Residencia:   Distrito
def mostrar_analisis_distrito_residencia(df_filtrado):
    st.subheader('Distribución por Distrito de Residencia')
    distritores_stats = analisis_distrito_residencia(df_filtrado)
    st.write(distritores_stats)

    distrito_counts = analisis_distrito_residencia(df_filtrado)
    fig_distrito = px.bar(distrito_counts, x=distrito_counts.index, y=distrito_counts.values, title='Distribución por Distrito de Residencia')
    st.plotly_chart(fig_distrito)

# Analisis de Residencia:   Provincia
def mostrar_analisis_provincia_residencia(df_filtrado):
    st.subheader('Distribución por Provincia de Residencia')
    provinciares_stats = analisis_provincia_residencia(df_filtrado)
    st.write(provinciares_stats)
    
    provincia_counts = analisis_provincia_residencia(df_filtrado)
    fig_provincia = px.bar(provincia_counts, x=provincia_counts.index, y=provincia_counts.values, title='Distribución por Provincia de Residencia')
    st.plotly_chart(fig_provincia)

# Analisis de Residencia:   Departamento
def mostrar_analisis_departamento_residencia(df_filtrado):
    st.subheader('Distribución por Departamento de Residencia')
    departamentores_stats = analisis_departamento_residencia(df_filtrado)
    st.write(departamentores_stats)
    departamento_counts = analisis_departamento_residencia(df_filtrado)
    fig_departamento = px.bar(departamento_counts, x=departamento_counts.index, y=departamento_counts.values, title='Distribución por Departamento de Residencia')
    st.plotly_chart(fig_departamento)

# Analisis de Modalidad
def mostrar_analisis_modalidad(df_filtrado):
    st.subheader('Distribución por Modalidad')
    modalidad_stats = analisis_modalidad(df_filtrado)
    st.write(modalidad_stats)
    modalidad_counts = analisis_modalidad(df_filtrado)
    fig_modalidad = px.pie(values=modalidad_counts.values, names=modalidad_counts.index, title='Distribución por Modalidad')
    st.plotly_chart(fig_modalidad)

# Analisis de Metodologia
def mostrar_analisis_metodologia(df_filtrado):
    st.subheader('Distribución por Metodología')
    metodoligia_stats = analisis_metodologia(df_filtrado)
    st.write(metodoligia_stats)
    metodologia_counts = analisis_metodologia(df_filtrado)
    fig_metodologia = px.bar(metodologia_counts, x=metodologia_counts.index, y=metodologia_counts.values, title='Distribución por Metodología')
    st.plotly_chart(fig_metodologia)

# Analisis por Facultad
def mostrar_analisis_facultad(df_filtrado):
    st.subheader('Distribución por Facultad')
    facultad_stats = analisis_facultad(df_filtrado)
    st.write(facultad_stats)
    facultad_counts = analisis_facultad(df_filtrado)
    fig_facultad = px.bar(facultad_counts, x=facultad_counts.index, y=facultad_counts.values, title='Distribución por Facultad')
    st.plotly_chart(fig_facultad)

# Analisis por Especialidad
def mostrar_analisis_especialidad(df_filtrado):
    st.subheader('Distribución por Especialidad')
    especialidad_stats = analisis_especialidad(df_filtrado)
    st.write(especialidad_stats)
    especialidad_counts = analisis_especialidad(df_filtrado)
    fig_especialidad = px.bar(especialidad_counts, x=especialidad_counts.index, y=especialidad_counts.values, title='Distribución por Especialidad')
    st.plotly_chart(fig_especialidad)

# Analisis de ciclo Relativo
def mostrar_analisis_ciclo_relativo(df_filtrado):
    st.subheader('Distribución por Ciclo Relativo')
    ciclorel_stats = analisis_ciclo_relativo(df_filtrado)
    st.write(ciclorel_stats)
    ciclo_relativo_counts = analisis_ciclo_relativo(df_filtrado)
    fig_ciclo_relativo = px.bar(ciclo_relativo_counts, x=ciclo_relativo_counts.index, y=ciclo_relativo_counts.values, title='Distribución por Ciclo Relativo')
    st.plotly_chart(fig_ciclo_relativo)

