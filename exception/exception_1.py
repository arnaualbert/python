




def check_int():

    num_str : str = input("escribe un entero : ")
    num: int = int(num_str)

    return num

if __name__ == "__main__":

    try:
        num : int = check_int()
        print(f"has escrito : {num}")
    except:
        print("Ha habido un error prueba de poner un numero")