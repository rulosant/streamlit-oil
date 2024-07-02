import streamlit as st

st.set_page_config(
    page_title="Oil&Gas Map Viewer",
    page_icon="👋",
    layout="wide",
)

st.write("# ¡Bienvenidos! 👋")

st.sidebar.success("Seleccione algún demo del menú.")

st.markdown(
    """

Utilizando la potencia de Streamlit creé en poco tiempo una aplicación web para la visualización de datos geoespaciales.
En este caso utilice fuentes de datos relacionadas con la industria Oil&Gas, la cual requiere de grandes capacidades de logística y organización. 
    
#### Usos

Contar con este tipo de aplicaciones permite a las compañías:
 * Compartir información con clientes e inversores.
 * Presentar planes de trabajo y avances de obra.
 * Contar con información sobre el entorno territorial, el equipamiento y las instalaciones.
 * Conectar con otros sistemas web o Apps mobile.
    
Esta web es una prueba de concepto para visualizar capas de datos de una forma sencilla y rápida.

Para el desarrollo se utilizó la librería [streamlit](https://docs.streamlit.io/) junto con los mapas de Folium y Leaflet.

#### Fuentes

Las capas que integran esta demo se obtienen de fuentes públicas como:
* COPADE Neuquén
* Secretaría de Energía de la Nación
* Subsecretaría de Telecomunicaciones de la Nación




"""
)

