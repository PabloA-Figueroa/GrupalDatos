import streamlit as st
import main
import resumen
from pathlib import Path
def show():
    st.markdown("""
    <style>
    .flex-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        gap: 20px;
    }
    .flex-item {
        flex: 1;
    }
    .flex-item img {
        max-width: 80%;
        height: auto;
    }
    .section-container {
        background-color: #f0f0f0; /* Color de fondo similar al "bg-muted" */
        padding: 50px 20px;
        text-align: center;
    }
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-top: 40px;
    }
    .grid-item {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    <h1 style="text-align: center;">Acerca del Conjunto de Datos</h1>
    <div class="flex-container">
        <div class="flex-item">
            <h2>INMET Paraná</h2>
            <p style="text-align: justify;">El presente proyecto se basa en el análisis de datos meteorológicos diarios provenientes del O BDMEP (Base de Dados Meteorológicas diárias em Forma Digital), una base de datos que recopila información de las estaciones meteorológicas convencionales de la red del INMET (Instituto Nacional de Meteorología). El conjunto de datos utilizado en este proyecto se limita a las estaciones ubicadas en el Estado del Paraná, Brasil.
            Varaibles: 
            Character:
                Municipio
                Factor:
                Tipo de clima
                Integer:
                Código de estación
                Día del año
                Numeric:
                Temperatura del aire
                Precipitación total
                Presión atmosférica al nivel de la estación
                Humedad relativa del aire
                Velocidad del viento
                Radiación global
                Temperatura máxima en la hora anterior
                Temperatura mínima en la hora anterior
                Temperatura del punto de rocío
                Temperatura máxima del punto de rocío en la hora anterior
                Temperatura mínima del punto de rocío en la hora anterior
                Presión atmosférica máxima en la hora anterior
                Presión atmosférica mínima en la hora anterior
                Rajada máxima de viento
                Dirección del viento por hora</p>
        </div>
        <div class="flex-item">
            <img src="https://miro.medium.com/v2/resize:fit:1358/0*jqxx3-dJqFjXD6FA" alt="Hero">
        </div>
    </div>
    <section style ='padding-bottom: 30px'; class="section-container">
        <div class="container">
            <div class="space-y-2">
                <div class="inline-block rounded-lg bg-muted px-3 py-1 text-sm">Data</div>
                <h2 class="text-3xl font-bold">Sobre los Datos que se predijieron</h2>
                <p class="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                    El conjunto de datos meteorológicos del Estado de
                    Paraná, Brasil, incluye variables como hora en UTC,
                    precipitación total horaria, presión atmosférica (al
                    nivel de la estación, máxima y mínima en la hora
                    anterior), radiación global, temperatura del aire y
                    del punto de rocío. El archivo cuenta con mas de 3M de datos.
                </p>
            </div>
        </div>
        <div style ='padding-top: 30px;padding-bottom: 30px;' class="grid-container">
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción de Precipitación Binaria</h3>
                <h4 class="text-sm text-muted-foreground" style="color: #6c757d;font-size: 1.25rem;">Precipitacion_Binaria</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                    Se predice la precipitación binaria para entender la ocurrencia de precipitaciones en función de diferentes factores climáticos. Esto ayuda a analizar patrones en la distribución de la precipitación y su impacto en el clima del estado de Paraná.
                </p>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción de Precipitación</h3>
                <h4 class="text-sm text-muted-foreground" style="color: #6c757d;font-size: 1.25rem;">Precipitacion</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                    Se predice la cantidad de precipitación diaria para examinar cómo varía en función de las condiciones meteorológicas y el tiempo. Esto permite identificar patrones y tendencias en la cantidad de precipitación en el estado de Paraná.
                </p>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción de Temperatura del Aire a Bulbo Seco Horaria</h3>
                <h4 class="text-sm text-muted-foreground" style="color: #6c757d;font-size: 1.25rem;">Temperatura_Aire_Bulbo_Seco_Horaria_C</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                    Se predice la temperatura del aire a bulbo seco horaria para comprender mejor las fluctuaciones diarias de la temperatura y cómo afectan el clima en el estado de Paraná. Esta variable es clave para analizar las condiciones térmicas en distintas horas del día.
                </p>
            </div>
        </div>
    </section>    
    """, unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Analisis de Datos - Curiosidades</h2>", unsafe_allow_html=True)
    # PCA y TSNE
    colPCA, colTSNE = st.columns(2)
    with colPCA:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;text-align: center;'>PCA</h2>", unsafe_allow_html=True)
        st.image("images/PCA.png", use_column_width=True, caption="PCA")
        st.markdown("<p style='text-align: justify;'>"
                    "Se observan que las primeras dos componentes principales (PC1 y PC2) explican una cantidad significativa de la varianza en los datos. PC1 explica aproximadamente el 28.86% de la varianza, mientras que PC2 explica el 22.26%. Juntas, PC1 y PC2 explican más del 51% de la varianza total en los datos."
                    "</p>", unsafe_allow_html=True)
    with colTSNE:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;text-align: center;'>BOXPLOT</h2>", unsafe_allow_html=True)
        st.image("images/BOXPLOT_BRASIL.png", use_column_width=True, caption="TSNE")
        st.markdown("<p style='text-align: justify;'>"
                    "Está gráfica nos permite observar diferencias claras en las temperaturas promedio y su variabilidad entre los diferentes municipios. Podemos identificar municipios con temperaturas más altas o más bajas, variabilidad en las temperaturas, y la presencia de valores atípicos. Esta información es útil para entender cómo el clima varía geográficamente y puede servir como base para estudios más detallados sobre los factores que influyen en estas diferencias de temperatura."
                    "</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='padding-top: 20px;padding-bottom: 20px;background-color: #f0f0f0;text-align: center;'>EDA</h2>", unsafe_allow_html=True)

    # EDA
    colEDA1, colEDA2 = st.columns(2)
    with colEDA1:
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Analsis</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>"
                    "Se observan que las primeras dos componentes principales (PC1 y PC2) explican una cantidad significativa de la varianza en los datos. PC1 explica aproximadamente el 28.86% de la varianza, mientras que PC2 explica el 22.26%. Juntas, PC1 y PC2 explican más del 51% de la varianza total en los datos."
                    "</p>", unsafe_allow_html=True)
    with colEDA2:
        st.image("images/EDA_BRASIL.png", use_column_width=True, caption="PCA")


    tipo1, tipo2 = st.columns(2)
    with tipo1:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;text-align: center;'>Precipitacion por municipio</h2>", unsafe_allow_html=True)
        st.image("images/PROMEDIOTEMPERATURA_RADIACION.png", use_column_width=True, caption="Precipitacion por municipio")
        st.markdown("<p style='text-align: justify;'>"
                    "Los resultados indican una clara tendencia ascendente, donde la temperatura promedio del aire aumenta con la radiación global, lo que es coherente con el hecho de que la radiación solar es una fuente principal de calentamiento del aire"
                    "</p>", unsafe_allow_html=True)
    with tipo2:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;text-align: center;'>Serie Temporal</h2>", unsafe_allow_html=True)
        st.image("images/SERIE_TEMPORAL.png", use_column_width=True, caption="PCA")
        st.markdown("<p style='text-align: justify;'>"
                    "La gráfica de serie temporal de la temperatura del aire es muy útil para entender la variabilidad estacional y diaria de la temperatura. Muestra claramente los patrones cíclicos asociados con las estaciones del año y resalta la variabilidad diaria. No parece haber un cambio significativo en el nivel general de las temperaturas a lo largo del tiempo"
                    "</p>", unsafe_allow_html=True)
    # PUNTOS IMPORTANTES IMAGENES
    st.markdown("<h2 style='padding-top: 20px;padding-bottom: 20px;background-color: #f0f0f0;text-align: center;'>RESULTADOS OBTENIDOS</h2>", unsafe_allow_html=True)

    # PUNTOS IMPORTANTES IMAGENES REGRESION LINEAL
    colRL1, colRL2 = st.columns(2)
    with colRL1:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/RANDOMFOREST_PRECIPITACION.png", use_column_width=True, caption="Resultados Obtenidos")
    with colRL2:
        # Titulo de la imagen
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Modelo Lineal</h2>", unsafe_allow_html=True)
        # Descripción de la imagen
        st.markdown("<p style='text-align: justify;'>"
                    "El Eje X representa las probabilidades predichas por el modelo de que haya lluvia. Va de 0 a 0.6 en el gráfico proporcionado, mientras que el. Eje Y: Representa la densidad de las probabilidades predichas. Esto indica cuán común es una probabilidad predicha específica en el conjunto de datos. "
                    "El gráfico indica  que el modelo parece ser bueno para predecir la ausencia de lluvia, tiene más dificultad para predecir la lluvia, y puede existir confusión ya que algunas probabilidades se sobreponen en las dos opciones de 'Lluvia' y 'No Lluvia', lo que indica que el modelo podría estar confundiendo algunas instancias de lluvia con no lluvia y viceversa."
                    "</p>", unsafe_allow_html=True)

    # PUNTOS IMPORTANTES IMAGENES RANDOM FOREST
    colRF1, colRF2 = st.columns(2)
    with colRF1:
        # Titulo de la imagen
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Regresion Logistica </h2>", unsafe_allow_html=True)
        # Descripción de la imagen
        st.markdown("<p style='text-align: justify;'>"
                    "La matriz de confusión muestra que el modelo tiene una alta precisión general del 96.33%, lo que indica que acierta en la mayoría de las predicciones. Sin embargo, la baja especificidad (0.0005) sugiere que el modelo tiene dificultades significativas para identificar correctamente las instancias de la clase negativa (0), mientras que su alta sensibilidad (0.99997) demuestra una capacidad casi perfecta para identificar la clase positiva (1). Esto puede estar relacionado con un desequilibrio en el conjunto de datos, donde la clase positiva es mucho menos frecuente. A pesar de la alta tasa de detección para la clase positiva, el bajo valor predictivo negativo (0.3611) y la baja estadística Kappa (9e-04) indican que el modelo no está mejorando mucho en comparación con una clasificación aleatoria y tiene problemas para generalizar a la clase negativa, lo que sugiere que se podrían necesitar ajustes adicionales para mejorar su rendimiento general."
                    ".</p>", unsafe_allow_html=True)
    with colRF2:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/RegresionLineal.png", use_column_width=True, caption="Resultados Obtenidos")
    #TITULO DE ARBOLES BINARIOS MD
    st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Arboles de Decision </h2>", unsafe_allow_html=True)
    # Arboles binarios
    colAB1, colAB2 = st.columns(2)
    with colAB1:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/ARBOLES_BINARIOS.png", use_column_width=True, caption="Resultados Obtenidos")
    with colAB2:
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Interpretacion</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>"
                    "Con el árbol de decisión se obtuvieron las siguientes métricas: el MSE es de aproximadamente 0.488, el RMSE es de aproximadamente 0.698, y el MAE es de aproximadamente 0.550. Estas métricas indican que, en promedio, las predicciones del modelo están a una distancia de 0.698 unidades de los valores reales, lo cual es relativamente pequeño y sugiere un buen rendimiento del modelo."
                    "</p>", unsafe_allow_html=True)

    # RANDOM FOREST 2
    colRF11, colRF12 = st.columns(2)
    with colRF11:
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Grafico de Dispersion</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>"
                    "Sin embargo, la gráfica de predicciones frente a valores reales muestra cierta dispersión, especialmente en los extremos, indicando que el modelo tiene más dificultades para predecir valores extremos con precisión."
                    "</p>", unsafe_allow_html=True)
    with colRF12:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/DISPERSION_AB.png", use_column_width=True, caption="Resultados Obtenidos")

    st.markdown("""
    <section style="padding-top: 30px;padding-bottom: 30px;" class="section-container">
        <div class="container">
            <div class="space-y-2">
                <h2 class="text-3xl font-bold">Valores Obtenidos</h2>
            </div>
        </div>
        <div class="grid-container">
            <div class="grid-item">
                <h3 class="text-lg font-bold">Regresion Lineal</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo de bosque aleatorio utilizado para predecir la variable objetivo.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">0.6</div>
                        <p class="text-muted-foreground">RMSE</p>
                    </div>
                </div>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Regresion logistica</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo utilizado para medir la relación entre la variable dependiente y una o más variables independientes.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">96%</div>
                        <p class="text-muted-foreground">Accuracy</p>
                    </div>
                </div>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Arboles de Decision</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo de árboles de decisión utilizado para predecir la variable objetivo.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">0.54</div>
                        <p class="text-muted-foreground">RSME</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div style="padding-top: 30px;padding-bottom: 30px;" class="flex-container">
        <div class="flex-item">
            <h2>DataSet Nacidos Vivos </h2>
            <p style="text-align: justify;">Este DataSet trata de los Registros Estadísticos de bebes Nacidos Vivos son investigaciones orientadas a cuantificar los hechos vitales ocurridos y/o inscritos en el Ecuador. La información recopilada en estos registros es esencial para la planificación de estrategias socio-económicas y proporciona a los sectores público y privado, uno de los instrumentos básicos para el análisis demográfico.</p>
        </div>
        <div class="flex-item">
        <img style="width: 400px; height: 100%;padding-left: 20px;" src="data:image/jpeg;base64,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" alt="Hero2">        
        </div>
    </div>

    <section class="section-container">
        <div class="container">
            <div class="space-y-2">
                <h2 class="text-3xl font-bold">Sobre los Datos que se predijieron</h2>
                <p  class="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                    El conjunto de datos contiene 230,381 observaciones y 47
                    variables relacionadas con nacimientos en 2023.
                    Información sobre el lugar de inscripción y nacimiento
                    (provincia, cantón, parroquia)
                    Fechas de inscripción y nacimiento, características del
                    recién nacido (sexo, talla, peso, semanas de gestación,
                    puntuaciones Apgar)
                    Tipo de parto, lugar de ocurrencia, asistencia durante
                    el parto, detalles de la madre (fecha de nacimiento,
                    edad, número de embarazos y partos, consultas
                    prenatales, etnia, estado civil, nivel de educación)
                    Area de residencia (urbana o rural).
                </p>
            </div>
        </div>
        <div class="grid-container">
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción del tipo de parto</h3>
                <h4 class="text-sm text-muted-foreground" style="color: #6c757d;font-size: 1.25rem;">Tipo_part</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                Se predijo esta variable para determinar el tipo de parto que se llevó a cabo en base a ciertos datos. Esto permite analizar patrones en los tipos de partos según la ubicación, la población o la edad de la madre.
                </p>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción de la edad materna</h3>
                <h4 class="text-sm text-muted-foreground"  style="color: #6c757d;font-size: 1.25rem;">Edad</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                Se predijo la edad de la madre en base a ciertos datos, lo que nos ayuda a identificar patrones en la edad de las madres, como el caso de las madres adolescentes, y a analizar su origen según la ubicación, la parroquia y otros factores.
                </p>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">Predicción de la inscripción</h3>
                <h4 class="text-sm text-muted-foreground" style="color: #6c757d;font-size: 1.25rem;">Peso</h4>
                <p style="text-align: justify;" class="text-sm text-muted-foreground">
                Se predijo esta variable para comprender por qué existen ciertos pesos en bebes en ciertos lugares, edades, tipos de parto y otros factores relevantes. Esto nos permite analizar patrones en los datos y mejorar nuestra comprensión de los factores que influyen en ellas.
                </p>
            </div>
        </div>
    </section>
    """ , unsafe_allow_html=True)
    colKNN1, colKNN2 = st.columns(2)
    with colKNN1:
         # Titulo de la imagen
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>KNN - Resultados Obtenidos</h2>", unsafe_allow_html=True)
        # Descripción de la imagen
        st.markdown("<p style='text-align: justify;'>"
                    "El modelo KNN utilizado para predecir el tipo de parto (cesárea o normal) tiene una precisión del 63.38%, con una sensibilidad del 63.40% para cesáreas y una especificidad del 63.35% para partos normales. Esto indica que el modelo predice correctamente la mayoría de los partos, pero tiene un margen de mejora en la identificación de cesáreas. Las variables que más influyen en la predicción son el peso del bebé, la talla del bebé, la edad de la madre, el número de controles prenatales, y la semana de gestación. Estas variables juegan un papel crucial en la diferenciación entre partos normales y cesáreas."
                    "</p>", unsafe_allow_html=True)
    with colKNN2:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/KNN_PARTO.png", use_column_width=True, caption="Resultados Obtenidos")

    colSVM1, colSVM2 = st.columns(2)
    with colSVM1:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/SVM.png", use_column_width=True, caption="Resultados Obtenidos SVM")
    with colSVM2:
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>SVM - Resultados Obtenidos</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: justify;'>"
                    "El modelo SVM utilizado para predecir el tipo de parto (cesárea o normal) tiene una precisión del 75.43%, con una sensibilidad del 63.49% para cesáreas y una especificidad del 87.53% para partos normales. Esto indica que el modelo predice correctamente la mayoría de los partos, pero tiene un margen de mejora en la identificación de cesáreas. Las variables que más influyen en la predicción son el peso del bebé, la talla del bebé, la edad de la madre, el número de controles prenatales, y la semana de gestación. Estas variables juegan un papel crucial en la diferenciación entre partos normales y cesáreas."
                    "</p>", unsafe_allow_html=True)
    colLMPESO1, colLMPESO2 = st.columns(2)
    with colLMPESO1:
         # Titulo de la imagen
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Regresion Lineal - Resultados Obtenidos</h2>", unsafe_allow_html=True)
        # Descripción de la imagen
        st.markdown("<p style='text-align: justify;'>"
                    "El modelo de regresión lineal utilizado para predecir el peso de los bebés tiene un error medio absoluto (MAE) de 0.62 y una raíz cuadrática del error medio (RMSE) de 0.79. Esto indica que el modelo tiene un margen de mejora en la predicción del peso de los bebés.Las variables más significativas en el modelo son la talla del bebé (talla), las semanas de gestación (sem_gest), el tipo de parto (tipo_partNormal), la edad de la madre (edad_mad), y los controles prenatales (con_pren)."
                    "</p>", unsafe_allow_html=True)
    with colLMPESO2:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/RegresionLinealPeso.png", use_column_width=True, caption=" Resultados Obtenidos")

    colAD1, colAD2 = st.columns(2)
    with colAD1:
        st.markdown("<h2 style='padding-top: 1px;padding-bottom: 1px;'></h2>", unsafe_allow_html=True)
        st.image("images/ArbolesD.png", use_column_width=True, caption="Resultados Obtenidos Arboles de Decision")
    with colAD2:
         # Titulo de la imagen
        st.markdown("<h2 style='text-align: center;padding-top: 30px;padding-bottom: 30px;'>Arboles de Decision - Resultados Obtenidos</h2>", unsafe_allow_html=True)
        # Descripción de la imagen
        st.markdown("<p style='text-align: justify;'>"
                    "El modelo de árbol de decisión se ajustó para predecir la edad de la madre utilizando un conjunto de datos de nacimientos. La importancia de las variables mostró que el número de partos (num_par) fue la variable más influyente, seguida del estado civil (est_civil), tipo de parto (tipo_part), provincia de inscripción (prov_insc) y provincia de residencia (prov_res). El modelo produjo un error medio absoluto (MAE) de 4.19, un error cuadrático medio (MSE) de 27.67, y una raíz del error cuadrático medio (RMSE) de 5.26. Las principales divisiones en el árbol se basaron en el número de partos y el estado civil, demostrando su alta relevancia en la predicción de la edad de la madre."
                    "</p>", unsafe_allow_html=True)

    st.markdown("""
    <section style="padding-top: 30px;padding-bottom: 30px;" class="section-container">
        <div class="container">
            <div class="space-y-2">
                <h2 class="text-3xl font-bold">Resultados Obtenidos</h2>
                <p class="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                </p>
            </div>
        </div>
        <div class="grid-container">
            <div class="grid-item">
                <h3 class="text-lg font-bold">Random Forest</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo de bosque aleatorio utilizado para predecir la variable objetivo.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">82%</div>
                        <p class="text-muted-foreground">Accuracy</p>
                    </div>
                </div>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">KNN</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo de vecinos más cercanos utilizado para predecir la variable objetivo.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">91.2%</div>
                        <p class="text-muted-foreground">Accuracy</p>
                    </div>
                </div>
            </div>
            <div class="grid-item">
                <h3 class="text-lg font-bold">SVM</h3>
                <p class="text-sm text-muted-foreground">
                    Modelo de árboles de decisión utilizado para predecir la variable objetivo.
                </p>
                <div class="p-6">
                    <div class="flex flex-col items-center justify-center space-y-4">
                        <div class="text-6xl font-bold">94%</div>
                        <p class="text-muted-foreground">RSME</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)





