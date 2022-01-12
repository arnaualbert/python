# una funcion que recive una lista y que devuelva un bool  true si encuentra el numero 3

def find_num3(num_list: list[int]) -> bool:

    index: int = 0
    found: bool = False
    out_of_range: bool = (index == len(num_list))
    finished: bool = found or out_of_range

    while not finished:

        num = num_list[index]
        found = (num == 3)

        index = index + 1
        out_of_range = (index == len(num_list))
        finished = found or out_of_range

    return found
