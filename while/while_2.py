def loop_02() -> list[int]:
    """return a list of 10 int"""

    count: int = 0
    finished: bool = (count == 10)

    result: list[int] = []

    while not finished:

        result.append(count)
        count: int = count + 1
        finished: bool = (count == 10)
        
    return result

# main
#-------------------------------------------------------------------------------------

num_list: list[int] = loop_02()

print(num_list)

#-------------------------------------------------------------------------------------