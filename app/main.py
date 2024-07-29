import os
# Configurar la variable de entorno R_HOME y añadir el directorio de la DLL de R
os.environ['R_HOME'] = r"C:\Program Files\R\R-4.3.2"
os.add_dll_directory(r"C:\Program Files\R\R-4.3.2\bin\x64")
import streamlit as st
import subprocess

# Función para hacer predicciones llamando al script R
def predict_precipitation_regresion_Lineal(presion, temperatura, humedad, municipio):
    command = [
        r"C:\Program Files\R\R-4.3.2\bin\x64\Rscript.exe",
        'C:/Users/PABLO/Documents/GrupalDatos/regresion.R',
        str(presion),
        str(temperatura),
        str(humedad),
        municipio
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
def show():
    # Configurar la interfaz de Streamlit
    st.title("Predicción de Precipitación")
    # Ver si el archivo .R esta en la ruta
    presion = st.number_input("Presión Atmosférica (mb)", value=1013.0)
    temperatura = st.number_input("Temperatura del Aire (C)", value=25.0)
    humedad = st.number_input("Humedad Relativa (%)", value=60.0)
    municipio = st.selectbox("Municipio", ["CAMPINA_DA_LAGOA", "Municipio2", "Municipio3"])  # Ajusta según tus datos

    if st.button("Predecir regresion Lineal"):
        prediccion = predict_precipitation_regresion_Lineal(presion, temperatura, humedad, municipio)
        st.write(f"Predicción de Precipitación: {prediccion} mm")
