import os

directorio_canal = directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'canal')
archivo = os.path.join(directorio_canal,'canal.txt')

with open(archivo, 'w') as file:
    file.write('todos')    