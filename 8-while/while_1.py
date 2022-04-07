# whiles loops
# while ejecuta el body mientras la condicion sea true


count: int = 0
finished: bool = (count > 3)


while not finished:

    # body
    print(count)

    # update finishing condition
    count = count + 1
    finished = (count > 3)
