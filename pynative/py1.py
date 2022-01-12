
count: int = 0
finished: bool = (count > 10)

while not finished:
    print(count)
    count = count + 1
    finished = (count > 10)

