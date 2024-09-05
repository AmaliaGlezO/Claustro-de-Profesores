import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import folium 
from streamlit_agraph import agraph, Node, Edge, Config

with open('antiguedad-matematica.csv', 'r') as f:
    file=pd.read_csv(f)
data=pd.DataFrame(file)
st.dataframe(data)
if 'Annos de servicio' in data.columns:
    # Reemplazar valores faltantes por None
    data['Annos de servicio'] = data['Annos de servicio'].fillna(None)

    # Calcular la antigüedad promedio por cargo
    antiguedad_promedio = data.groupby('Cargo')['Annos de servicio'].mean().reset_index(name='Antigüedad Promedio')

    # Crear el gráfico de barras
    fig = px.bar(antiguedad_promedio, 
                 x='Cargo', 
                 y='Antigüedad Promedio', 
                 title='Antigüedad Promedio de Profesores por Cargo',
                 color='Antigüedad Promedio',
                 color_continuous_scale=px.colors.sequential.Viridis)

    # Personalizar el diseño del gráfico
    fig.update_traces(hoverinfo='x+y')
    fig.update_layout(margin=dict(t=50, l=0, r=0, b=0),
                      xaxis_title='Cargo',
                      yaxis_title='Antigüedad Promedio (años)',
                      yaxis=dict(tickmode='linear'))

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
else:
    st.error("La columna 'Años de servicio' no se encuentra en el DataFrame.")
