import os
import random 
from subprocess import PIPE, Popen, STDOUT

# with open(archivo, 'r') as file:
#     file_content = file.read()

# print(file_content)

directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')
capitulos_ya_vistos = []

def obtenerCapituloRandom():
  carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
  carpetas_filtradas = [nombre for nombre in carpetas if nombre != "01-comerciales"]
  carpeta_random = random.choice(carpetas_filtradas)

  ruta_carpeta = os.path.join(directorio, carpeta_random)
  episodio = random.choice(os.listdir(ruta_carpeta))
  ruta_completa = os.path.join(ruta_carpeta, episodio)
  return ruta_completa

def obtenerComerciales():
  carpeta_comerciales = os.path.join(directorio, "01-comerciales")
  comerciales = [(os.path.join(carpeta_comerciales, nombre)) for nombre in os.listdir(carpeta_comerciales) if os.path.isfile(os.path.join(carpeta_comerciales, nombre))]
  comerciales_seleccionados = random.sample(comerciales, 3)
  return comerciales_seleccionados

def reproducirVideos():
  global capitulos_ya_vistos
  encontrado = True

  while(encontrado):
    capitulo = obtenerCapituloRandom()
    if capitulo not in capitulos_ya_vistos:
      encontrado = False

  playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', capitulo])
  playProcess.wait()

  capitulos_ya_vistos.append(capitulo)

  comerciales = obtenerComerciales()

  for comercial in comerciales:
    playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', comercial])
    playProcess.wait()


while (True):
  reproducirVideos()

# cmd = "nohup omxplayer -b -o hdmi "+"'"+ruta_carpeta+episodio+"' &"
# os.system('killall omxplayer.bin')
# os.system(cmd)
