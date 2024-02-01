#Importar bibliotecas y descargar recursos adicionales NLTK
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import numpy as np
import math

#Cargar datos desde un archivo Excel
data = pd.read_excel("/content/DatasetsUnificado.xlsx")

#Extraer columnas de resumenes
abstract_gt = data["Abstract real"]
abstract_gpt = data["Abstract artificial"]
#Convertir las columnas a listas
abstract_gt = list(abstract_gt)
abstract_gpt = list(abstract_gpt)

def nlp(documento):
  #Eliminar caracteres no alfabéticos y números
  documento = re.sub('[^A-Za-z0-9]+',' ',documento)
  #Convertir a minúsculas
  documento = documento.lower()
  #Tokenizar el documento en palabras
  documento = word_tokenize(documento)
  #Eliminar stopwords
  stop_words = set(stopwords.words("english"))
  words = []
  for word in documento:
    if word not in stop_words:
      words.append(word)
  #Aplicar el proceso de stemming a las palabras
  steemer = PorterStemmer()
  steaming=[]
  for word in words:
    steaming.append(steemer.stem(word))

def getDiccionario(documentos):
  #Construir y retornar un diccionario de términos
  diccionario = []
  for list_words in documentos:
    for word in list_words:
      if word not in diccionario:
        diccionario.append(word)
  return diccionario

def matriz_binaria(diccionario, documentos):
  #Construir y retornar una matriz binaria
  matriz = np.zeros((len(diccionario), len(documentos)))
  for index, word in enumerate(diccionario, start=0):
    for indexd, documento in enumerate(documentos, start=0):
      if word in documento:
        matriz[index, indexd] = 1
  return matriz

def overlap(a, b):
  #Calcular y retornar el coeficiente de Overlap entre dos conjuntos
  intersection = np.logical_and(a, b)
  similarity = (intersection.sum()) / min(a.sum(), b.sum())
  return similarity
#Inicializar contador y lista para almacenar resultados
k = 0
total_overlap = []
while k < len(abstract_gt):
  #Procesar los resúmenes reales y artificiales
  lista = [abstract_gt[k], abstract_gpt[k]]
  res = []
  for documento in lista:
    res.append(nlp(documento))
  #Construir diccionario y matriz binaria
  diccionario = getDiccionario(res)
  matriz_title = matriz_binaria(diccionario, res)
  matriz_distancia = np.zeros((matriz_title.shape[1], matriz_title.shape[1]))
  #Calcular la matriz de distancias utilizando el coeficiente de Overlap
  i = 0
  while i < matriz_title.shape[1]:
    j = 0
    while j < matriz_title.shape[1]:
      matriz_distancia[i][j] = overlap(matriz_title[:,i], matriz_title[:,j])
      j+=1
    i+=1
  #Incrementar el contador y almacenar el resultado
  k+=1
  matriz_distancia = matriz_distancia
  total_overlap.append(matriz_distancia[0][1])
#Crear DataFrame y guardar resultados en un archivo CSV
df = pd.DataFrame(total_overlap)
df.to_csv("results_overlap.csv")
