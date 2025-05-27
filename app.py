import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv('vehicles_us.csv')

# Titulo  de la aplicación
st.title('Analysis of Car Sales Ads (USA)')

# Encabezado
st.header('Interactive Data Exploration')

# Checkbox para mostrar los datos de Histograma
show_histogram = st.checkbox('Show Histogram of odometer')
if show_histogram:
    st.subheader('Milage Distribution (Odometer)')
    fig = px.histogram(df, x='odometer', nbins=50,
                       title='Histogram of Odometer')
    st.plotly_chart(fig)

# Checkbox para mostrar los datos de Scatter Plot (odmometer vs price)
show_scatter = st.checkbox('Show Scatter Plot of Odometer vs Price')
if show_scatter:
    st.subheader('Odometer vs Price')
    fig2 = px.scatter(df, x='odometer', y='price',
                      title='Scatter Plot of Odometer vs Price')
    st.plotly_chart(fig2, use_container_width=True)
