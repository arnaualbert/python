count: int = 7
cf: list[int] = [6,5,4,3,2,1]
finished: bool = (count < 1)

while not finished:
    count = count - 1
    cf.remove(count)
    print(cf)
    finished = (count < 1)