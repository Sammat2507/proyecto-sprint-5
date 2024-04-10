import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('C:\\Users\\samue\\OneDrive\\Documents\\triple ten\\Sprint 5\\proyecto-sprint-5\\vehicles_us.csv')
st.header('Car data')
histogram_button = st.button('Construir histograma')

if histogram_button:
    st.write('Construyendo histograma de kilometraje')

    hist_odometer = px.histogram(car_data, x='odometer')

    st.plotly_chart(hist_odometer, use_container_width=True)

dispersion_button = st.button('Construir dispersion')

if dispersion_button:
    st.write('Construyendo grafico de dispersion de kilometraje')

    disp_odometer = px.scatter(car_data, x='odometer', y='price')
