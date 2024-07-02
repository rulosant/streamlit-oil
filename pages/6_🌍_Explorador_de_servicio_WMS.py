import ast
import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Selector de capas obtenidas de fuentes públicas.

Ejemplo provisto por OpenGeo
"""

st.sidebar.title("About")
st.sidebar.info(markdown)



@st.cache_data
def get_layers(url):
    options = leafmap.get_wms_layers(url)
    return options


st.title("Web Map Service (WMS)")
st.markdown(
    """
Esta sección permite visualizar un mapa y de forma dinámica, agregar capas obtenidos de otros servidores. En esta caso las capas se obtienen de la Secretaría de Energía.
"""
)

row1_col1, row1_col2 = st.columns([3, 1.3])
width = None
height = 600
layers = None

with row1_col2:

    #esa_landcover = "https://services.terrascope.be/wms/v2"
    esa_landcover = "https://sig.energia.gob.ar/wmsenergia"
    
    #url = st.text_input(
    #    "Enter a WMS URL:", value="https://sig.energia.gob.ar/wmsenergia"
    #)

    url = 'https://sig.energia.gob.ar/wmsenergia'
    empty = st.empty()

    if url:
        options = get_layers(url)

        default = None
        if url == esa_landcover:
            #default = "WORLDCOVER_2020_MAP"
            default = "planosbase_yacimientos"
            
        layers = empty.multiselect(
            "Seleccionar las capas para agregar al mapa:", options, default=default
        )

        if default == "epen_eett":
            legend = str(leafmap.builtin_legends["planosbase_yacimientos"])
        else:
            legend = ""


    with row1_col1:
        m = leafmap.Map(center=[-38.085, -68.873], zoom=8)

        if layers is not None:
            for layer in layers:
                m.add_wms_layer(
                    url, layers=layer, name=layer, attribution=" ", transparent=True
                )

        m.to_streamlit(width, height)