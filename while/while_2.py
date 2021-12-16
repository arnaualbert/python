# whiles loops
#while ejecuta el body mientras la condicion sea true

def loop_02() -> list[int]:
    """return a list of 10 int"""

    count = 0
    finished: bool = (count == 10)

    result: list[int] = []

    while not finished:

        result.append(count)
        count = count + 1
        finished = (count == 10)
        

    return result

print(loop_02())