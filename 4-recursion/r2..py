from pathlib import Path

def get_dir(bases: Path):


    base = Path(bases)
    if (base.is_dir()):

        path_list = sorted(base.glob("*"))

        for path in path_list:
            get_dir(path)
    
    lista = []
    if (base.is_file()):
        lista.append(base.name)
        print(lista)
    
    return lista





    

get_dir(".")