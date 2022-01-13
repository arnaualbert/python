cf = [10, 20, 30, 40, 50]
count: int = 50
finished: bool = (count < 10)

while not finished:
    count = count - 10
    cf.remove(count)
    print(cf)
    finished = (count < 10)