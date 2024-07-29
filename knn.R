# prediccion_knn.R
library(class)
library(dplyr)
library(caret)

# Función para normalizar los datos
normalize_data <- function(data, mean_vals, sd_vals) {
  return((data - mean_vals) / sd_vals)
}

# Leer los argumentos de la línea de comandos
args <- commandArgs(trailingOnly = TRUE)

# Convertir los argumentos en variables
talla <- as.numeric(args[1])
peso <- as.numeric(args[2])
sem_gest <- as.numeric(args[3])

# Cargar el modelo guardado
model <- readRDS("C:/Users/PABLO/Documents/DATOS_ZORIN/DATOS/GRUPAL_DATOS/modelo_knn_reducido.rds")

# Cargar los datos utilizados para la normalización
train_data_numeric <- readRDS("C:/Users/PABLO/Documents/DATOS_ZORIN/DATOS/GRUPAL_DATOS/train_data_numeric_reducido.rds")

# Calcular medias y desviaciones estándar de los datos de entrenamiento
mean_vals <- apply(train_data_numeric, 2, mean)
sd_vals <- apply(train_data_numeric, 2, sd)

# Crear un nuevo data frame con los datos de entrada
new_data <- data.frame(
  talla = talla,
  peso = peso,
  sem_gest = sem_gest
)

# Normalizar los datos de entrada
new_data_normalized <- normalize_data(new_data, mean_vals, sd_vals)

# Hacer la predicción
prediccion <- knn(train = model$train_data_normalized, test = new_data_normalized, cl = model$train_labels, k = model$best_k)

# Imprimir la predicción
print(prediccion)
