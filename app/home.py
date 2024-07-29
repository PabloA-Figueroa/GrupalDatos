import streamlit as st
st.set_page_config(
    page_title="Home",
    page_icon="👋",
    layout="wide",
)
import main
import informacion as info
import regresionPeso
# Configurar la página

st.markdown("""
    <style>
    /* Hide the link button */
    .stApp a:first-child {
        display: none;
    }
    
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    </style>
    """, unsafe_allow_html=True)
# Configurar el menú de navegación
left_column, right_column = st.columns(2)
with left_column:
    st.markdown("<h1 style='text-align: center;'>TRABAJO GRUPAL SEGUNDO BIMESTRE - UTPL</h1>", unsafe_allow_html=True)
with right_column:
    st.image('images/images.png')
info1,main1,regresionP = st.tabs(["Información","Regresión Lineal","Regresion Lineal Peso"])
with info1:
    info.show()
with main1:
    main.show()
with regresionP:
    regresionPeso.show()

