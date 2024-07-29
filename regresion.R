args <- commandArgs(trailingOnly = TRUE)
# Seleccionar las variables de interés
features <- c('Precipitacion_Total_Horaria_mm', 'Presion_Atmosferica_Estacion_Horaria_mb',
              'Temperatura_Aire_Bulbo_Seco_Horaria_C', 'Humedad_Relativa_Aire_Horaria', 'Municipio')

Presion_Atmosferica_Estacion_Horaria_mb <- as.numeric(args[1])
Temperatura_Aire_Bulbo_Seco_Horaria_C <- as.numeric(args[2])
Humedad_Relativa_Aire_Horaria <- as.numeric(args[3])
Municipio <- as.factor(args[4])
# Imprimir los valores
# Cargar el modelo guardado
model <- readRDS("C:/Users/PABLO/Documents/DATOS_ZORIN/DATOS/GRUPAL_DATOS/modelo_precipitacion.rds")
# Verificar que el modelo se haya cargado correctamente
# Crear un nuevo data frame con los datos de entrada
new_data <- data.frame(
  Presion_Atmosferica_Estacion_Horaria_mb = Presion_Atmosferica_Estacion_Horaria_mb,
  Temperatura_Aire_Bulbo_Seco_Horaria_C = Temperatura_Aire_Bulbo_Seco_Horaria_C,
  Humedad_Relativa_Aire_Horaria = Humedad_Relativa_Aire_Horaria,
  Municipio = Municipio
)

# Hacer la predicción
prediccion <- predict(model, new_data)
# Imprimir la predicción
print(prediccion)
