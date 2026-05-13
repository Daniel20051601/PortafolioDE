import streamlit as st
from utils.image_to_base64 import get_base64
from ui.segmentos.tecnologias import segmento_tecnologias
from ui.segmentos.proyectos import segmento_proyectos
from ui.segmentos.contactame import segmento_contactame

st.set_page_config(
    page_title="Mi Portafolio",
    page_icon="🚀",
    menu_items={
        'Get Help': 'https://www.tu-web.com/contacto',
        'Report a bug': "https://github.com/Daniel20051601/issues",
        'About': " Este es mi portafolio profesional desarrollado con Streamlit."
    }
)

img_base64 = get_base64("assets/images/profile/profile3.png")

st.markdown(
    f"""
    <div style="display: flex; justify-content: center;">
        <img src="data:image/jpg;base64,{img_base64}"
             width="200"
             style="border-radius: 50%;">
    </div>
    """,
    unsafe_allow_html=True
)

st.title('Ramón Emilio López', text_alignment='center')

st.caption("""
Estudiante de :red[Ingeniería en Sistemas] apasionado por el área de :red[**Ingeniería de Datos**], la automatización y el aprendizaje continuo, con experiencia en desarrollo de software y en la creación de soluciones orientadas al procesamiento e integración eficiente de datos.
""", text_alignment= 'center')

st.space('large')


col1, col2, col3, col4 = st.columns([2,1,1,2])

with col2: 
    st.link_button(" GitHub", "https://github.com/Daniel20051601", 
        icon=":material/code:", 
        type = 'tertiary',
        key='go_to_github') 
with col3: 
    st.link_button(" LinkedIn", "www.linkedin.com/in/ramón-emilio-lopez-57a833211", 
        icon=":material/work:", 
        type = 'tertiary',
        key='go_to_linkedin')

st.space('medium')

segmento_tecnologias()

st.space('small')

segmento_proyectos()

st.space('small')

segmento_contactame()


