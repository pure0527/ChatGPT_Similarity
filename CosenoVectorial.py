#Importar bibliotecas y descargar recursos adicionales NLTK
import numpy as np
import math
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
import re

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
  return steaming

def getDiccionario(documentos):
  #Construir y retornar un diccionario de términos únicos
  diccionario = []
  for list_words in documentos:
    for word in list_words:
      if word not in diccionario:
        diccionario.append(word)
  return diccionario

def tf(diccionario, documentos):
  #Construir y retornar una matriz TF
  matriz = np.zeros((len(diccionario), len(documentos)))
  for index, word in enumerate(diccionario, start=0):
    for indexd, documento in enumerate(documentos, start=0):
      if word in documento:
        matriz[index, indexd] = documento.count(word)
  return matriz

def wtf(tf):
  #Aplicar la función Wtf a una matriz TF
  matriz_wtf = np.zeros(tf.shape)
  i = 0
  while i < tf.shape[0]:
    j = 0
    while j < tf.shape[1]:
      if tf[i][j] == 0:
        matriz_wtf[i][j] = 0
      else:
        matriz_wtf[i][j] = 1 + math.log(tf[i][j], 10)
      j+=1
    i+=1
  return matriz_wtf

def df(wtf):
  #Calcular y retornar un vector DF
  matriz_df = np.zeros((wtf.shape[1]))
  i = 0
  while i < wtf.shape[1]:
    j = 0
    sum = 0
    while j < wtf.shape[0]:
      if wtf[j][i] != 0:
        sum+=1
      j+=1
    matriz_df[i] = sum
    i+=1
  return matriz_df

def idf(df, n):
  #Calcular y retornar un vector IDF
  matriz_idf = np.zeros((df.shape[0]))
  i = 0
  while i < df.shape[0]:
    matriz_idf[i] = math.log((n/df[i]), 10)
    i+=1
  return matriz_idf

def tfxidf(wft, idf):
  #Calcular y retornar una matriz TFxIDF
  return np.multiply(wft, idf)

def normalizar_vectores(wtf):
  #Calcular y retornar vectores normalizados
  modulos = np.zeros((wtf.shape[1]))
  vector_u = np.zeros(wtf.shape)
  i = 0
  while i < modulos.shape[0]:
    modulos[i] = math.sqrt(sum(pow(element, 2) for element in wtf[:,i]))
    i+=1

  i = 0
  while i < wtf.shape[1]:
    j = 0
    while j < wtf.shape[0]:
      vector_u[j][i] = wtf[j][i] / modulos[i]
      j+=1
    i+=1
  return vector_u

def cos(a, b):
  #Calcular y retornar el coseno entre dos vectores
  multi = np.multiply(a, b)
  return multi.sum()

#Inicializar contadores y listas para almacenar resultados
k = 0
sum1 = 0
sum2 = 0
sumtotal = 0
total_cos = []
while k < len(abstract_gt):
  #Procesar resúmenes reales y artificiales
  lista = [abstract_gt[k], abstract_gpt[k]]
  res = []

  for documento in lista:
      res.append(nlp(documento))
      sumtotal+=len(nlp(documento))

  #Calcular y normalizar matrices TF-IDF y vectores normalizados
  diccionario = getDiccionario(res)
  matriz_tf = tf(diccionario, res)
  matriz_wtf = wtf(matriz_tf)
  vector_df = df(matriz_wtf)
  vecto_idf = idf(vector_df, matriz_wtf.shape[1])
  matriz_tfxidf = tfxidf(matriz_wtf, vecto_idf)
  vector_u = normalizar_vectores(matriz_tfxidf)
  matriz_distancia = np.zeros((vector_u.shape[1], vector_u.shape[1]))

  #Calcular y almacenar distancias coseno entre vectores normalizados
  i = 0
  while i < vector_u.shape[1]:
      j = 0
      while j < vector_u.shape[1]:
          aux = cos(vector_u[:,i], vector_u[:,j])
          matriz_distancia[i][j] = aux
          j+=1
      i+=1

  #Almacenar resultados parciales y actualizar sumatorias
  total_cos.append(matriz_distancia[0][1])
  sum1 += matriz_distancia[0][1]
  sum2 += matriz_distancia[1][0]
  df1 = pd.DataFrame(matriz_distancia)
  k+=1
  
#Calcular estadísticas y guardar resultados en un archivo CSV
df = pd.DataFrame(total_cos)
df.to_csv("results_coseno.csv")