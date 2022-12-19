import os
import shutil
import random

class Pregunta:

  def __init__(self, texto, opciones, respuesta):
    self.texto = texto
    self.opciones = opciones
    self.respuesta = respuesta

  def es_correcta(self, respuesta_seleccionada):
    return respuesta_seleccionada == self.respuesta


# Creamos algunas preguntas de ejemplo
pregunta1 = Pregunta("¿Cuál es el animal más grande del mundo?",
                     ["Ballena azul", "Elefante", "Rinoceronte"],
                     "Ballena azul")
pregunta2 = Pregunta("¿Cuál es la capital de Francia?",
                     ["Londres", "París", "Nueva York"], "París")
pregunta3 = Pregunta("¿Cuántos continentes hay en el mundo?", ["6", "7", "8"],
                     "7")

# Creamos una lista de preguntas
banco_preguntas = [pregunta1, pregunta2, pregunta3]

# La ruta de la carpeta que quieres verificar
folder_path = "preguntas"

# La ruta de la carpeta que quieres verificar
folder_path_r = "respuestas"

# Verifica si la carpeta NO existe
if not os.path.exists(folder_path):
  #si la carpeta no existe, la creamos
  os.mkdir(folder_path)

# Verifica si la carpeta NO existe
if not os.path.exists(folder_path_r):
  #si la carpeta no existe, la creamos
  os.mkdir(folder_path_r)
  
#creamos un arreglo de examenes
examenes = []

# Itera sobre un rango de números del 1 al 21
for i in range(1, 21):
  # Construye el nombre del archivo
  filename = f"preguntas{i}.txt"

  # Construye la ruta completa del archivo, incluyendo la carpeta
  filepath = folder_path + "/" +filename

  #creamos una lista depreguntas vacia
  preguntas = []
  #obtenemos 20 preguntas aleatorias
  for j in range(0,10):
    # Obtiene un índice aleatorio del array
    indice_aleatorio = random.randint(0, len(banco_preguntas) - 1)
    #extraemos la pregunta del banco usando el indice_aleatorio
    pregunta = banco_preguntas[indice_aleatorio]
    #agregamos la pregunta a la lista de preguntas
    preguntas.append(pregunta)
  #agregamos las preguntas del examen al arreglo de examenes
  examenes.append(preguntas)
  # Abre el archivo en modo de escritura
  with open(filepath, "w") as f:
    # Itera sobre la lista de preguntas
    for pregunta in preguntas:
      # Escribe la pregunta en el archivo y agrega una nueva línea
      f.write(pregunta.texto + "\n")
      #Iteramos para obtener las opciones y las escribimos dando un salto de linea al final
      for opcion in pregunta.opciones:
        #Escribimos las opciones que existen en esta pregunta
        f.write(opcion + "\n")
      #Agregamos un salto de lines al final para pasar a la siguiente pregunta
      f.write("\n")

# Zipea la carpeta y guarda el archivo en el mismo directorio
shutil.make_archive(folder_path, "zip", folder_path)




i = 0;
# Itera sobre un rango de números del 1 al 21
for examen in examenes:
  # Construye el nombre del archivo
  filename_r = f"preguntas_con_respuesta{i+1}.txt"
  #añadimos 1 al indice
  i = i+1
  # Construye la ruta completa del archivo, incluyendo la carpeta
  filepath_r = folder_path_r + "/" +filename_r

# Abre el archivo en modo de escritura
  with open(filepath_r, "w") as f:
    # Itera sobre la lista de preguntas
    for pregunta in examen:
      # Escribe la pregunta en el archivo y agrega una nueva línea
      f.write(pregunta.texto + "\n")
      #Iteramos para obtener las opciones y las escribimos dando un salto de linea al final
      for opcion in pregunta.opciones:
        f.write(opcion + "\n")
      #Agregamos la respuesta correcta
      f.write("La respuesta correcta es: "+ pregunta.respuesta + "\n")
      #Agregamos un salto de lines al final para pasar a la siguiente pregunta
      f.write("\n")

# Zipea la carpeta y guarda el archivo en el mismo directorio
shutil.make_archive(folder_path_r, "zip", folder_path_r)
