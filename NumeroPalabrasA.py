#Importar la biblioteca de Pandas
import pandas as pd 

#Definir el nombre del archivo de conferencia
conferencia = "gpt-icmla_2015.csv"

#Leer el conjunto de datos desde un archivo CSV
dataset = pd.read_csv(f"./content/Dataset Artificiales/{conferencia}", encoding="utf-8", sep=",")

#Imprimir el número de artículos en la conferencia
print(f"Numero de articulos {len(dataset)}")

#Extraer la columna de resúmenes
abstracts = dataset["0"]

#Función para calcular el mínimo de palabras en una serie de texto
def minimo_palabras(data):
    minimo = 1000
    for row in data:
        words = row.split(" ")
        if minimo > len(words):
            minimo = len(words)

    return minimo

#Función para calcular el máximo de palabras en una serie de texto
def maximo_palabras(data):
    maximo = 0
    for row in data:
        words = row.split(" ")
        if maximo < len(words):
            maximo = len(words)

    return maximo

#Función para contar palabras en una serie de texto
def contador_palabras(data):
    sum = 0
    for row in data:
        words = row.split(" ")
        sum += len(words)

    return sum

#Calcular y mostrar estadísticas sobre el número de palabras en los resúmenes
media_abstract = contador_palabras(abstracts) / len(abstracts)
print(f"Promedio palabras conferencia {conferencia} por abstract = {media_abstract}")
print(f"Minimo palabras conferencia {conferencia} por abstract = {minimo_palabras(abstracts)}")
print(f"Maximo palabras conferencia {conferencia} por abstract = {maximo_palabras(abstracts)}")
