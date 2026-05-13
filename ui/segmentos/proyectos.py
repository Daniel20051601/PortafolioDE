import streamlit as st
from data.info import PROJECTS

def segmento_proyectos():
    tab, = st.tabs(["Proyectos"])
    
    with tab:
        for p in PROJECTS:
            container_project(p['url_image'], p['title'], p['description'], p['url_link'], p['list_technologies'])


def container_project(url_image, title, description, url_link, list_technologies):
    
    with st.container(border=True, width='stretch'):
        col1, col2 = st.columns([1,2])
        
        with col1:
            st.image(url_image, width='stretch')
            
        with col2:
            st.subheader(title)
            st.write(f"{description[:150] + '...' if len(description) > 150 else description}")
            
            text = " ".join(
                f":red-badge[{t}]"
                for t in list_technologies
                )
            st.markdown(text)
            
            st.link_button("Detalles",url=url_link, type='tertiary')
    