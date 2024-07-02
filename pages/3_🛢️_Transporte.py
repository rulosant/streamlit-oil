import streamlit as st
import folium
from streamlit_folium import folium_static
import requests
import folium.plugins as plugins

# Título de la aplicación
st.title("Transporte")

# Crear un mapa folium/
mapa = folium.Map(location=[-38.085, -68.873], zoom_start=8)




# Configuración de la barra lateral
st.sidebar.title("Oleoductos")

show_wms_layer = st.sidebar.checkbox("Ductos", value=True)
if show_wms_layer:
    # Crear capa WMS
    wms_url = "https://sig.energia.gob.ar/wmsenergia"
    layer_name = "planosbase_ductos"

    wms_layer = folium.raster_layers.WmsTileLayer(
        url=wms_url,
        name=layer_name,
        layers=layer_name,
        transparent=True,
        opacity=0.5
    )

    wms_layer.add_to(mapa)




show_geojson_layer_ductos = st.sidebar.checkbox("Oleoductos", value=True)


# Obtener la capa Oleoductos COPADE
geojson_url_ductos = "https://giscopade.neuquen.gov.ar/geoserver/Copade/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=Copade:oleoductos&outputFormat=application%2Fjson"
geojson_response_ductos = requests.get(geojson_url_ductos)
geojson_data_ductos = geojson_response_ductos.json()

geojson_layer_ductos = folium.GeoJson(
    geojson_data_ductos,
    name="Oleoductos"
)
if show_geojson_layer_ductos:
    geojson_layer_ductos.add_to(mapa)

#show_red_vial_layers = st.sidebar.checkbox("Red Vial", value=False)



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
if show_wms_layer or show_red_vial_layers:
    folium.LayerControl().add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

# Información adicional en la barra lateral
st.sidebar.title("Información de las Capas")
st.sidebar.write("Datos obtenidos de capas públicas")
