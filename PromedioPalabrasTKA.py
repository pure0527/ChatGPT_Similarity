#Importar la biblioteca de Pandas
import pandas as pd 

#Definir el nombre del archivo de conferencia
conferencia = "ICMLA_2015.csv"

#Leer el conjunto de datos desde un archivo CSV
dataset = pd.read_csv(f"./content/Dataset Reales/{conferencia}", encoding="cp1252", sep=";")

#Extraer columnas del titulo, resumen y palabras clave
titles = dataset[dataset.keys()[0]]
abstracts = dataset[dataset.keys()[2]]
keywords = dataset[dataset.keys()[1]]

#Función para contar palabras en una serie de texto
def contador_palabras(data):
    sum = 0
    for row in data:
        words = row.split(" ")
        sum += len(words)

    return sum

#Calcular el promedio de palabras por título, palabras clave y resumen
media_title = contador_palabras(titles) / len(titles)
media_abstract = contador_palabras(abstracts) / len(abstracts)
media_keyword = contador_palabras(keywords) / len(keywords)

print(f"Promedio palabras conferencia {conferencia} por titulo = {media_title}, keywords = {media_keyword}, abstract = {media_abstract}")
