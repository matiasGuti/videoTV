import os
import random 
from subprocess import PIPE, Popen, STDOUT

directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')
capitulos_ya_vistos = []

#La funciona ingresara al archivo /canal/canal.txt y sacara dentro del archivo el nombre del canal actual
def obtenerCanalActual():
  directorio_canal = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'canal', 'canal.txt')
  
  with open(directorio_canal, 'r') as file:
      canal = file.read()

  return canal

#La funciona elegira un capitulo al azar dentro de la carpeta del canal actual
def obtenerCapituloRandom():
  canal = obtenerCanalActual()
  directorio_capitulos = os.path.join(directorio, canal)
  carpetas = [nombre for nombre in os.listdir(directorio_capitulos) if os.path.isdir(os.path.join(directorio_capitulos, nombre))]
  ruta_carpeta = os.path.join(directorio_capitulos, random.choice(carpetas))
  episodio = random.choice(os.listdir(ruta_carpeta))
  ruta_completa = os.path.join(ruta_carpeta, episodio)

  return ruta_completa

#La funcion armara un arreglo de "N" comerciales al azar, donde "N" es elegido por el usuario
def obtenerComerciales(n_comerciales):
  canal = obtenerCanalActual()
  carpeta_comerciales = os.path.join(directorio, "01-comerciales", canal)
  comerciales = [(os.path.join(carpeta_comerciales, nombre)) for nombre in os.listdir(carpeta_comerciales) if os.path.isfile(os.path.join(carpeta_comerciales, nombre))]
  comerciales_seleccionados = random.sample(comerciales, n_comerciales)

  return comerciales_seleccionados

#La funcion reproducira un capitulo elegido al azar (siempre que no haya salido ya) y un set de "N" comerciales despues del capitulo
def reproducirVideos():
  global capitulos_ya_vistos
  encontrado = True

  while(encontrado):
    capitulo = obtenerCapituloRandom()
    if capitulo not in capitulos_ya_vistos:
      encontrado = False

  #Reproducir video
  playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', capitulo])
  playProcess.wait()

  capitulos_ya_vistos.append(capitulo)

  comerciales = obtenerComerciales(n_comerciales=3)

  for comercial in comerciales:
    #Reproducir video
    playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'fill', comercial])
    playProcess.wait()


while (True):
  reproducirVideos()


# cmd = "nohup omxplayer -b -o hdmi "+"'"+ruta_carpeta+episodio+"' &"
# os.system('killall omxplayer.bin')
# os.system(cmd)
