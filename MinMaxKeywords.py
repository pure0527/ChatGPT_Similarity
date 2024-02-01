#Importar la biblioteca de Pandas
import pandas as pd 

#Leer el conjunto de datos desde un archivo CSV
dataset = pd.read_csv("./content/Dataset Reales/ICMLA_2015.csv", encoding="cp1252", sep=";")

#Imprimir las primeras filas del conjunto de datos
print(dataset.head())

#Extraer la columna de palabras clave
keywords = dataset[dataset.keys()[1]]

sum = []
for row in keywords:
    words = row.split(" ")
    sum.append(len(words))
    
#Calcular y mostrar el número mínimo y máximo de palabras clave por entrada
print(min(sum))
print(max(sum))