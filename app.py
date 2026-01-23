import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv('Datos/vehicles_us.csv')

st.header('US Vehicles')
st.dataframe(datos)
boton = st.checkbox('Histograma')

if boton:
    grafico = px.histogram(datos, x='odometer')
    st.plotly_chart(grafico)


