args <- commandArgs(trailingOnly = TRUE)

# Convertir argumentos a las variables correspondientes
talla <- as.numeric(args[1])
sem_gest <- as.numeric(args[2])
tipo_part <- as.factor(args[3])
apgar1 <- as.numeric(args[4])
apgar5 <- as.numeric(args[5])
edad_mad <- as.numeric(args[6])
con_pren <- as.numeric(args[7])
num_emb <- as.factor(args[8])
num_par <- as.numeric(args[9])
etnia <- as.factor(args[10])
est_civil <- as.factor(args[11])
niv_inst <- as.factor(args[12])
# Cargar el modelo guardado
model <- readRDS("C:/Users/PABLO/Documents/DATOS_ZORIN/DATOS/GRUPAL_DATOS/modelo_regresion_peso.rds")
# Crear un nuevo data frame con los datos de entrada
new_data <- data.frame(
  talla = talla,
  sem_gest = sem_gest,
  tipo_part = tipo_part,
  apgar1 = apgar1,
  apgar5 = apgar5,
  edad_mad = edad_mad,
  con_pren = con_pren,
  num_emb = num_emb,
  num_par = num_par,
  etnia = etnia,
  est_civil = est_civil,
  niv_inst = niv_inst
)
# Hacer la predicción
prediccion <- predict(model, new_data)

# Imprimir la predicción y variables
print(prediccion/20)