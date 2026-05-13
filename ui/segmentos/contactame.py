import streamlit as st

def segmento_contactame():
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        st.link_button(":material/Mail: Contáctame", "mailto:danielvilopez@gmail.com", type='primary', key='cont_email')
        
        