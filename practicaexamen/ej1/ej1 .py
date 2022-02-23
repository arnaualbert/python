from importlib.resources import path
from   pathlib import Path
from   typing  import Iterator

import shutil
import sys

import engine

def get_txt(txt_file: str):

    #coge el archivo lo lee y le saca los espacios
    inv: str = Path("friends.txt").read_text()
    strp_txt: str = inv.strip()

    #poner los cuatro nombres en la lista
    lista_nombres: list[str] = strp_txt.split(",")
    lista_str_nombres: list[str] = [(txt_str) for txt_str in lista_nombres]
    metadata_list: list[dict] = [(txt_str) for txt_str in lista_nombres]
    print(metadata_list)
    #llenar espacios
    # llenar_espacios : str = "invitation.txt"
    # vars_dict : dict = {"entry_list": zip(lista_str_nombres,meta)}
    # txt_str: str = engine.fill_template(llenar_espacios,vars_dict)

    # for nombre in 
get_txt("friends.txt") 

