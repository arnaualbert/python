from ast import arg
from os import rename
from pathlib import Path
from re import S
from typing import Iterator
import shutil

def change_name(archivos: list[str],nuevos_archivos: list[str]):

    # archivos_dir: Path = archivos
    # iter_archivos : Iterator[Path] = archivos_dir
    # list_archivos: list[Path] = (iter_archivos)

    # for archivo in archivos:    
    #     if archivo == "a1.txt":
    #         rename("a1.txt","b1.txt")
    #     elif archivo == "a2.txt":
    #         rename("a2.txt","b2.txt")
    #     elif archivo == "a3.txt":
    #         rename("a3.txt","b3.txt")
    # rename("./archivos/a1.txt","b1.txt")

    # for archivo in archivos:
    #     for nuevo in nuevos_archivos:
    #         if archivo == "a1.txt":
    #             a = rename(archivo,nuevo)
    #             shutil.copy(a, nuevo)
    #         elif archivo == "a2.txt":
    #             b= rename(archivo,nuevo)
    #             shutil.copy(b)
    #         elif archivo == "a3.txt":
    #             c = rename(archivo,nuevo)
    #             shutil.copy(c)

    # for archivo in archivos:
    #     if archivo == "a1.txt":
    #         rename(archivo,nuevos_archivos[0])
    #     elif archivo == "a2.txt":
    #         rename(archivo,nuevos_archivos[1])
    #     elif archivo == "a3.txt":
    #         rename(archivo,nuevos_archivos[2])
    for archivo in archivos:
        if archivo == archivos[0]:
            rename(archivo,nuevos_archivos[0])
        elif archivo == archivos[1]:
            rename(archivo,nuevos_archivos[1])
        elif archivo == archivos[2]:
            rename(archivo,nuevos_archivos[2])

change_name(["a1.txt","a2.txt","a3.txt"],["b1.txt","b2.txt","b3.txt"])