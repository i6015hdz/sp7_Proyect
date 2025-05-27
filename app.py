import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Titulo  de la aplicación
st.title('Analysis of Car Sales Ads (USA)')

# Encabezado
st.header('Interactive Data Exploration')

# Botón para histograma
if st.button('Display Odometer Histogram'):
    st.write('Mileage distribution (odometer)')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Scatter Plot: Display odometer vs price '):
    st.write('Relationship between odometer and price')
    fig2 = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
