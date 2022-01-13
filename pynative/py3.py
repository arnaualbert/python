def get_calculate():
    a: int = int(input("Di un numero: "))
    b: int = 0
    finished: bool = (a < 0)

    while not finished:
        b = b + a
        a = a - 1
        finished = (a < 0)
    print(b)


get_calculate()
