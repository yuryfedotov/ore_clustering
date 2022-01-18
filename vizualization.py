import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Визуализация кластеров в трехмерном пространстве")

df = pd.read_csv("clustering.csv", delimiter=";")

fig = px.scatter_3d(
    data_frame=df,
    x='Содержание Fe',
    y='Магнетит',
    z='Доля класса -5мм',
    color='Кластер',
    size_max=1
)

st.plotly_chart(fig, use_container_width=False)