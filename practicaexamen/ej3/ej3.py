# import psutil
import os
def get_espacio(saber_espacio):
    total = 0
    for dirpath, dirnames, filenames in os.walk(saber_espacio):
        for fname in filenames:
            total += os.stat(os.path.join(dirpath, fname)).st_size

print(get_espacio("./ej3"))