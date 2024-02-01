#Importar bibliotecas y descargar recursos adicionales NLTK
import pandas as pd 
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')

#Definir el nombre del archivo de conferencia
conferencia = "ICMLA_2015.csv"
#Leer el conjunto de datos desde un archivo CSV
dataset = pd.read_csv(f"./content/Dataset Reales/{conferencia}", encoding="cp1252", sep=";")

#Extraer la columna de resúmenes
abstracts = dataset[dataset.keys()[2]]

#Función para procesar el texto con técnicas de procesamiento de lenguaje natural (NLP)
def nlp(documento):
    documento = re.sub('[^A-Za-z0-9]+',' ',documento)
    documento = documento.lower()
    documento = word_tokenize(documento)
    n_tokens = len(documento)
    stop_words = set(stopwords.words("english"))
    words = []
    for word in documento:
        if word not in stop_words:
            words.append(word)
    return [words, n_tokens]

#Función para realizar el stemming en una lista de palabras
def steaming_(words):
    steemer = PorterStemmer()
    steaming=[]
    for word in words:
        steaming.append(steemer.stem(word))
    return steaming

#Función para obtener el diccionario de palabras de una lista de documentos
def getDiccionario(documentos):
    diccionario = []
    for list_words in documentos:
        for word in list_words:
            if word not in diccionario:
                diccionario.append(word)
    return diccionario

#Listas para almacenar resultados
res = []
res_steaming = []
sumtotal = 0
sumtotal2 = 0
sumtotal3 = 0

#Procesar cada documento en los resúmenes
for documento in abstracts:
    aux, aux3 = nlp(documento)
    res.append(aux)
    aux2 = steaming_(aux)
    res_steaming.append(aux2)
    sumtotal+=len(aux)
    sumtotal2+=len(aux2)
    sumtotal3+=aux3

#Obtener el diccionario de palabras
diccionario = getDiccionario(res)

#Imprimir estadísticas y resultados
print(f"Suma total de tokens {sumtotal3 / len(abstracts)}")
print(f"Suma total de tokens {sumtotal2 / len(abstracts)} quitando las stopwords")
print(f"Suma total de tokens {sumtotal / len(abstracts)} con steaming")
print(f"Total de palabras en el diccionario {len(diccionario)}")
