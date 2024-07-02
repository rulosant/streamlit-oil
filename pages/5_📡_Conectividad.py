import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import folium.plugins as plugins

# Título de la aplicación
st.title("Conectividad")

# Crear un mapa folium/
mapa = folium.Map(location=[-38.085, -68.873], zoom_start=6)


# Configuración de la barra lateral
st.sidebar.title("Conectividad")

# REFEFO Json
show_geojson_layer = st.sidebar.checkbox("Red Federal de Fibra Optica", value=True)

geojson_url = "https://www.idecom.gob.ar/geoserver/idera/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=idera%3Aa010503-TRAZA-FO&outputFormat=application%2Fjson&bbox=-78.9854,-45.1452,-62.9836,-35.4950"
geojson_response = requests.get(geojson_url)
geojson_data = geojson_response.json()

geojson_layer = folium.GeoJson(
    geojson_data,
    name="Red Federal de Fibra Optica",
    style_function=lambda feature: {
        "fillColor": "#00ff00",
        "color": "green",
        "weight": 2,
    }    
)
if show_geojson_layer:
    geojson_layer.add_to(mapa)


# Antenas 3G 4G
show_antenas = st.sidebar.checkbox("Antenas 2G / 3G / 4G", value=False)
if show_antenas:

    # Obtener la capa GeoJSON Antenas
    geojson_url_antenas = "https://www.idecom.gob.ar/geoserver/publico/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=publico%3Aa010502-ANTENAS&outputFormat=application%2Fjson&bbox=-78.9854,-45.1452,-62.9836,-35.4950"
    geojson_response_antenas = requests.get(geojson_url_antenas)
    geojson_data_antenas = geojson_response_antenas.json()

    geojson_layer_antenas = folium.GeoJson(
        geojson_data_antenas,
        marker = folium.Marker(icon=folium.Icon(
                                     icon_color='#ff033e',
                                     icon='certificate',
                                     prefix='fa')), 
        name="Antenas 2G / 3G / 4G"
    )

    geojson_layer_antenas.add_to(mapa)

# Configuración de la barra lateral
st.sidebar.title("Red Vial")


# Obtener la capa GeoJSON Red Vial Principal
show_red_vial_layers = st.sidebar.checkbox("Red Vial", value=False)

geojson_url_redvial_principal = "https://www.idecom.gob.ar/geoserver/base/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=base%3Aa307-CAMN-RedVialPrincipal&outputFormat=application%2Fjson&bbox=-78.9854,-41.1452,-62.9836,-37.4950"
geojson_response_redvial_principal = requests.get(geojson_url_redvial_principal)
geojson_data_redvial_principal = geojson_response_redvial_principal.json()

geojson_layer_redvial_principal = folium.GeoJson(
    geojson_data_redvial_principal,
    name="Red Vial Principal",
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
        "dashArray": "5, 5",
    }
)

# Obtener la capa GeoJSON Red Vial Secundaria
geojson_url_redvial_secundaria = "https://www.idecom.gob.ar/geoserver/base/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=base%3Aa308-CAMP-RedVialsecundaria&outputFormat=application%2Fjson&bbox=-78.9854,-41.1452,-62.9836,-37.4950"
geojson_response_redvial_secundaria = requests.get(geojson_url_redvial_secundaria)
geojson_data_redvial_secundaria = geojson_response_redvial_secundaria.json()

geojson_layer_redvial_secundaria = folium.GeoJson(
    geojson_data_redvial_secundaria,
    name="Red Vial Secundaria"
)


if show_red_vial_layers:

    geojson_layer_redvial_principal.add_to(mapa)
    geojson_layer_redvial_secundaria.add_to(mapa)



# Añadir las capas según la selección



# Añadir control de capas si hay al menos una capa seleccionada
if show_red_vial_layers or show_geojson_layer:
    folium.LayerControl().add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

# Información adicional en la barra lateral
st.sidebar.title("Información de las Capas")
st.sidebar.write("Datos obtenidos de capas públicas")
