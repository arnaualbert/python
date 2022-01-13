def get_first10():
    count: int = 0
    finished: bool = (count > 10)

    while not finished:
        print(count)
        count = count + 1
        finished = (count > 10)


get_first10()
