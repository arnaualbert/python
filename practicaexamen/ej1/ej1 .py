
from pathlib import Path
import shutil
import engine

def get_txt(txt_file: Path):

    #coge el archivo lo lee y le saca los espacios
    inv: str = Path("friends.txt").read_text()
    names_list: list[str] = inv.split(",")
    # strp_txt: str = inv.strip()
    #poner los cuatro nombres en la lista
    # lista_nombres: list[str] = strp_txt.split(",")
    # lista_str_nombres: list[str] = [(txt_str) for txt_str in lista_nombres]
    # metadata_list: list[dict] = [(txt_str) for txt_str in lista_nombres]
    # print(metadata_list)
    #llenar espacios
    # llenar_espacios : str = "invitation.txt"
    # vars_dict : dict = {"entry_list": zip(lista_str_nombres,meta)}
    # txt_str: str = engine.fill_template(llenar_espacios,vars_dict)
    # list_nombres: list[str] = list(inv)
    # name_list = [inv]
    # for nombre in inv:
    #     name_list.append(nombre)
    print(names_list)
    for name in names_list:
        if name == names_list[0]:
            engine.fill_template(name)
            shutil.copy("./input/invitation.txt","./invitation1.txt")
        elif name == names_list[1]:
            engine.fill_template(name)
            shutil.copy("./input/invitation.txt","./invitation2.txt")
        elif name == names_list[2]:
            engine.fill_template(name)
            shutil.copy("./input/invitation.txt","./invitation3.txt")



get_txt("/ej1/friends.txt") 

