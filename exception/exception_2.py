def check_seq():

    seq_str : str = input("dime una sequencia de longitud multiple de tres: ")

    long_seq = len(seq_str)

    return long_seq

if __name__ == "__main__":

    try:
        sequencia : str = check_seq()
        print(f"has escrito : {sequencia}")
    except:
        print("Ha habido un error prueba de poner un numero")