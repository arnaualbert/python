def get_seq():

    seq_str : str = input("dime una sequencia de longitud multiple de tres: ")

    long_seq : bool = ((len(seq_str) % 3) == 0)

    if not long_seq:
        raise Exception("no es divisible de 3")

    return seq_str

if __name__ == "__main__":

    try:
        sequencia : str = get_seq()
        print(f"has escrito : {sequencia}")
    except:
        print("Ha habido un error prueba de poner otra sequencia")