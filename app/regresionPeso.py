import os
# Configurar la variable de entorno R_HOME y añadir el directorio de la DLL de R
os.environ['R_HOME'] = r"C:\Program Files\R\R-4.3.2"
os.add_dll_directory(r"C:\Program Files\R\R-4.3.2\bin\x64")
import streamlit as st
import subprocess

# Función para hacer predicciones llamando al script R
def predict_peso(talla, sem_gest, tipo_part, apgar1, apgar5, edad_mad, con_pren, num_emb, num_par, etnia, est_civil, niv_inst):
    command = [
        r"C:\Program Files\R\R-4.3.2\bin\x64\Rscript.exe",
        'C:/Users/PABLO/Documents/GrupalDatos/regresionPeso.R',
        str(talla),
        str(sem_gest),
        tipo_part,
        str(apgar1),
        str(apgar5),
        str(edad_mad),
        str(con_pren),
        str(num_emb),
        str(num_par),
        etnia,
        est_civil,
        niv_inst
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def show():
    st.title("Predicción de Peso del Bebé")

    # Entradas del usuario
    talla = st.number_input("Talla (cm)", value=50.0)
    sem_gest = st.number_input("Semanas de Gestación", value=40.0)
    tipo_part = st.selectbox("Tipo de Parto", ["Normal", "Cesárea", "Otro"])
    apgar1 = st.number_input("APGAR al minuto 1", value=8.0)
    apgar5 = st.number_input("APGAR a los 5 minutos", value=9.0)
    edad_mad = st.number_input("Edad de la Madre", value=30.0)
    con_pren = st.number_input("Controles Prenatales", value=10.0)
    num_emb = st.text_input("Número de Embarazos", value="2")
    num_par = st.number_input("Número de Partos", value=1.0)
    etnia = st.selectbox("Etnia", ["Mestiza", "Etnia2", "Etnia3"])
    est_civil = st.selectbox("Estado Civil", ["Soltera", "Casada", "Divorciada", "Otro"])
    niv_inst = st.selectbox("Nivel de Instrucción", ["Ninguno", "Educación Básica", "Secundaria", "Otro"])

    if st.button("Predecir Peso del Bebé"):
        prediccion = predict_peso(talla, sem_gest, tipo_part, apgar1, apgar5, edad_mad, con_pren, num_emb, num_par, etnia, est_civil, niv_inst)
        st.write(f"Predicción del Peso del Bebé: {prediccion} kg")
