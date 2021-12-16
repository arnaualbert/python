# whiles loops
#while ejecuta el body mientras la condicion sea true

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

print(loop_02())