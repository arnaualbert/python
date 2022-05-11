




def check_int():

    num_str : str = input("escribe un entero : ")
    num: int = int(num_str)

    return num

if __name__ == "__main__":

    num : int = check_int()

    print(f"has escrito : {num}")