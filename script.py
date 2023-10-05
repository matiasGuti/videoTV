import os
import random 
import time
from subprocess import PIPE, Popen, STDOUT

directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

capitulos_ya_vistos = []

def obtenerCapituloRandom():
  carpetas = [nombre for nombre in os.listdir(directorio) if os.path.isdir(os.path.join(directorio, nombre))]
  carpetas_filtradas = [nombre for nombre in carpetas if nombre != "comerciales"]
  carpeta_random = random.choice(carpetas_filtradas)

  ruta_carpeta = os.path.join(directorio, carpeta_random)
  episodio = random.choice(os.listdir(ruta_carpeta))
  ruta_completa = os.path.join(ruta_carpeta, episodio)
  return ruta_completa

def obtenerComerciales():
  carpeta_comerciales = directorio + "\\comerciales"
  archivos = [nombre for nombre in os.listdir(carpeta_comerciales) if os.path.isfile(os.path.join(carpeta_comerciales, nombre))]
  archivos_seleccionados = random.sample(archivos, 3)
  return archivos_seleccionados

def reproducirVideos():
  print("------- Revision --------")
  global capitulos_ya_vistos
  encontrado = True

  while(encontrado):
    capitulo = obtenerCapituloRandom()
    print(capitulo)
    if capitulo not in capitulos_ya_vistos:
      encontrado = False

  capitulos_ya_vistos.append(capitulo)
  print(capitulos_ya_vistos)
  return(capitulo)
  
# print(obtenerCapituloRandom())
# print(obtenerComerciales())

i=0
while (i<3):
  reproducirVideos()
  i += 1

# cmd = "nohup omxplayer -b -o hdmi "+"'"+ruta_carpeta+episodio+"' &"
# os.system('killall omxplayer.bin')
# os.system(cmd)
