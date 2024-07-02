import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Mapa dividido mostrando dos capas obtenidas de fuentes públicas.

Ejemplo provisto por OpenGeo
"""

st.sidebar.title("About")
st.sidebar.info(markdown)


st.title("Mapa dividido")



m = leafmap.Map(center=[-38.085, -68.873], zoom=8)
m.split_map(
    left_layer="OpenTopoMap", right_layer="ESA WorldCover 2020"
)
m.add_legend(title="ESA Land Cover", builtin_legend="ESA_WorldCover")

m.to_streamlit(height=700)