import streamlit as st
from data.info import PROJECTS

def segmento_proyectos():
    tab, = st.tabs(["Proyectos"])
    
    with tab:
        for p in PROJECTS:
            container_project(p['url_image'], p['title'], p['description'],p['list_technologies'], p['url_code'], p['url_link'])


def container_project(url_image, title, description, list_technologies, url_code, url_link):
    
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
            
            botones = []
            if url_code:
                botones.append(("Código", url_code, ":material/code:"))
            if url_link:
                botones.append(("Visitar", url_link, ":material/globe:"))

            if botones:
                col1, _ = st.columns(2, gap='xxsmall')
                with col1:
                    for label, url, icon in botones:
                        st.link_button(label, url=url, type='tertiary', icon=icon)
                    
            
    