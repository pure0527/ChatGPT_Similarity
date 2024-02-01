#!pip install openai
import openai
from datetime import datetime
import pandas as pd

openai.api_key = "api-key"

#Cargar la conferencia de manera local
conferencia = "ICMLA_2015.csv"
#Leer un archivo CSV con pandas, usando cp1252 como codificación y punto y coma como separador.
dataset = pd.read_csv(f"/content/ICMLA_2015.csv", encoding="cp1252", sep=";")

titles = dataset[dataset.keys()[0]]
lonAbstract = dataset[dataset.keys()[2]]

res = []
i = 0
#Registrar el tiempo de inicio.
start_time = datetime.now()
#Bucle para generar resúmenes artificiales
while i < len(lonAbstract):
  #Crea una pregunta para solicitar la generación de un abstract basado en el título y el abstract existente.
  pregunta = "You can generate an abstract from this title of a scientific article '{0}'. It must be a maximum of {1} words. No line breaks, a single paragraph.".format(titles[i], lonAbstract[i])
  #Utiliza OpenAI's ChatCompletion API para generar el abstract.
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [{"role": "system", "content" : pregunta}]
  )
  respuesta = completion.choices[0].message.content
  res.append(respuesta)
  print(titles[i])
  i+=1
#Calcular el tiempo transcurrido
time_elapsed = datetime.now() - start_time
print('Tiempo transcurrido (hh:mm:ss.ms) {}'.format(time_elapsed))
df = pd.DataFrame(res)
print(df)
#Crea un DataFrame con las respuestas generadas y lo guarda en un archivo CSV.
df.to_csv(f"abstracts_gpt_{conferencia}.csv")