#Importar bibliotecas y descargar recursos adicionales NLTK
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

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
    return steaming