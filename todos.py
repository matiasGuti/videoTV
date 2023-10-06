import os

directorio_canal = directorio = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'canal', 'canal.txt')

with open(directorio_canal, 'w') as file:
    file.write('todos')    