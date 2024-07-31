import streamlit as st
# Estilo personalizado para cambiar el fondo
st.set_page_config(
    page_title="Dashboard con Gráfico Animado de Plotly",
    layout="wide",
    initial_sidebar_state="expanded",
    #theme="light"  # Configura el tema a 'light' para evitar el tema oscuro del navegador
)
# Configurar la aplicación de Streamlit
if __name__ == "__main__":
    st.title('Análisis')

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import PIL as Image
from analisis import analisis_genero, analisis_ciclo_relativo
from cargar_datos import cargar_datos

# Cargar los datos
df = cargar_datos()

def analisis_genero1(df_filtrado):
    genero_counts = df_filtrado['genero'].value_counts()
    genero_stats = genero_counts.to_frame('count').assign(porcentaje=lambda x: (x['count'] / x['count'].sum()) * 100)
    return genero_stats

def mostrar_analisis_genero(df_filtrado):
    st.subheader('Distribución de Género')
    genero_stats = analisis_genero(df_filtrado)
    st.write(genero_stats)
    
    genero_counts = analisis_genero(df_filtrado)
    if genero_counts.empty:
        st.write("No hay datos para mostrar.")
        return
    colors = ['lightgreen', 'darkorange']
    fig = go.Figure(
        data=[go.Pie(
            labels=genero_counts.index,
            values=genero_counts.values
        )])
    fig.update_traces(
        hoverinfo='label+percent', 
        textinfo='value', 
        textfont_size=20, 
        marker=dict(colors=colors, line=dict(color='white', width=2))
    )
    st.plotly_chart(fig, use_container_width=True)
    labels=genero_counts.index
    values=genero_counts.values
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
    fig.update_traces(
        hoverinfo='label+percent', 
        textinfo='value', 
        textfont_size=20, 
        marker=dict(colors=colors, line=dict(color='#000000', width=3))
    )
    #st.plotly_chart(fig)


#cuadro incuAd
df= px.data.tips()
values = [100, 90, 80,70,60,50,40,30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["",#contenedor total
        "container", "A1","A2", "A3","A3", "A4", "A5", "A6",
        "container", "B1", "B2"
    ]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Reds'
))
st.plotly_chart(fig)


def mostrar_analisis_genero1(df_filtrado):
    st.subheader('Distribución de Género')
    genero_stats = analisis_genero(df_filtrado)
    st.write(genero_stats)
    
    genero_counts = analisis_genero(df_filtrado)
    colors = ['lightgreen', 'darkorange']
    labels = genero_counts.index
    values = genero_counts.values
    
    fig_genero = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.4)])
    fig_genero.update_traces(
        hoverinfo='label+percent', 
        textinfo='value', 
        textfont_size=20, 
        marker=dict(colors=colors, line=dict(color='black', width=3))
    )
    
    st.plotly_chart(fig_genero)


fig = go.Figure(
    data=[go.Scatter(x=[0, 1], y=[0, 1])],
    layout=go.Layout(
        xaxis=dict(range=[0, 5], autorange=False),
        yaxis=dict(range=[0, 5], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                        method="animate",
                        args=[None])])]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 2], y=[1, 2])]),
            go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
            go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])],
                    layout=go.Layout(title_text="End Title"))]
) 
#st.plotly_chart(fig)
