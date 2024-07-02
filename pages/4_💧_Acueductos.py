import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import folium.plugins as plugins

# Título de la aplicación
st.title("Acueductos")

# Crear un mapa folium/
mapa = folium.Map(location=[-37.3684, -69.1109], zoom_start=11)





# Acueductios

# Configuración de la barra lateral
st.sidebar.title("Acueductos")

show_geojson_layer_acueductos = st.sidebar.checkbox("Acueductos", value=True)


geojson_url_acueductos = "https://giscopade.neuquen.gov.ar/geoserver/Copade/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Copade:oleoductos&outputFormat=application%2Fjson"
geojson_response_acueductos = requests.get(geojson_url_acueductos)
geojson_data_acueductos = geojson_response_acueductos.json()

geojson_layer_acueductos = folium.GeoJson(
    geojson_data_acueductos,
    name="Acueductos",
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "yellow",
        "weight": 2,
    }        
)
if show_geojson_layer_acueductos:
    geojson_layer_acueductos.add_to(mapa)




# Añadir las capas según la selección



# Añadir control de capas si hay al menos una capa seleccionada
if show_geojson_layer_acueductos:
    folium.LayerControl().add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

# Información adicional en la barra lateral
st.sidebar.title("Información de las Capas")
st.sidebar.write("Datos obtenidos de capas públicas")
