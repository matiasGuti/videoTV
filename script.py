import os
import random 
from subprocess import PIPE, Popen, STDOUT

directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')
capitulos_ya_vistos = []

def obtenerCanalActual():
  #Obtener path del archivo txt donde esta el canal actual
  directorio_canal = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'canal', 'canal.txt')
  
  #Leer archivo txt y guardar en una variable el canal actual
  with open(directorio_canal, 'r') as file:
      canal = file.read()

  return canal

def obtenerCapituloRandom():
  canal = obtenerCanalActual()
  directorio_capitulos = os.path.join(directorio, canal)
  carpetas = [nombre for nombre in os.listdir(directorio_capitulos) if os.path.isdir(os.path.join(directorio_capitulos, nombre))]
  ruta_carpeta = os.path.join(directorio_capitulos, random.choice(carpetas))
  episodio = random.choice(os.listdir(ruta_carpeta))
  ruta_completa = os.path.join(ruta_carpeta, episodio)

  return ruta_completa

def obtenerComerciales():
  canal = obtenerCanalActual()
  carpeta_comerciales = os.path.join(directorio, "01-comerciales", canal)
  comerciales = [(os.path.join(carpeta_comerciales, nombre)) for nombre in os.listdir(carpeta_comerciales) if os.path.isfile(os.path.join(carpeta_comerciales, nombre))]
  comerciales_seleccionados = random.sample(comerciales, 4)

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
