#Cargar bibliotecas
library(readr)
library(ggplot2)

#Leer los resultados de diferentes índices de similitud desde archivos CSV
results_coseno <- read_csv("C:/Users/Nicker/Downloads/results_coseno.csv",  col_types = cols(...1 = col_skip()))
results_jaccard <- read_csv("C:/Users/Nicker/Downloads/results_jaccard.csv", col_types = cols(...1 = col_skip()))
results_sorensen <- read_csv("C:/Users/Nicker/Downloads/results_sorensen.csv", col_types = cols(...1 = col_skip()))
results_overlap <- read_csv("C:/Users/Nicker/Downloads/results_overlap.csv", col_types = cols(...1 = col_skip()))

#Combinar todos los datos en un marco de datos
todos_los_datos <- rbind(
  transform(results_coseno, conjunto = "Coseno"),
  transform(results_jaccard, conjunto = "Jaccard"),
  transform(results_sorensen, conjunto = "Sorensen"),
  transform(results_overlap, conjunto = "Overlap")

)

#Crear un gráfico de densidad
ggplot(todos_los_datos, aes(x = X0, fill = conjunto)) +
  geom_density(alpha = 0.5) +  #Usa geom_density para crear las campanas de Gauss
  labs(title = "Distribuciones de probabilidades",
       x = "Valor",
       y = "Densidad") +
  scale_color_discrete(name = "Índices") +
  theme_minimal()

#Resumen estadístico de los resultados de las métricas de similitud
summary(results_coseno$0)
summary(results_jaccard$0)
summary(results_sorensen$0)
summary(results_overlap$0)

#Calcular desviación estándar
sd(results_coseno$0)
sd(results_jaccard$0)
sd(results_sorensen$0)
sd(results_overlap$0)
