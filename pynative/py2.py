def get_pattern():
    count: int = 0
    cf: list[int] = []
    finished: bool = (count > 4)

    while not finished:
        count = count + 1
        cf.append(count)
        print(cf)
        finished = (count > 4)


get_pattern()
