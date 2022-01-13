count: int = 6
cf: list[int] = []
finished: bool = (count < 1)

while not finished:
    count = count - 1
    cf.append(count)
    print(cf)
    finished = (count < 1)