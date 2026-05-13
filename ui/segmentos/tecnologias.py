import streamlit as st
from data.info import TECHNOLOGIES

def segmento_tecnologias():
    tab, = st.tabs(["Tecnologías"])
    
    with tab:
        tecnologias = TECHNOLOGIES
        text = " ".join(
            f":red-badge[**{t}**]"
            for t in tecnologias
        )
        
        st.markdown(text)