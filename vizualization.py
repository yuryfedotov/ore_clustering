import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Визуализация кластеров в четырехмерном пространстве")

"""

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

"""

df = pd.read_csv("clustering.csv", delimiter=";")

nlmk_blue = "#051C2C"
nlmk_navy = "#00A9F4"
nlmk_red = "#E5546C"
nlmk_orange = "#FAA082"

color_map = {
    0: nlmk_blue,
    1: nlmk_navy,
    2: nlmk_red,
    3: nlmk_orange
}

fig = px.scatter_3d(
    data_frame=df,
    x='Содержание Fe',
    y='Магнетит',
    z='Доля класса -5мм',
    color='Кластер',
    color_discrete_map=color_map,
    size_max=1
)

# Plot!
#st.plotly_chart(fig, use_container_width=True)
st.plotly_chart(fig, use_container_width=False)