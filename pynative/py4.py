def get_mult():
    b: int = int(input("Di la tabla de multiplicar que quieres: "))
    a: int = b
    finished: bool = (a == b * 10)

    while not finished:
        a = a + b
        print(a)
        finished = (a == b * 10)


get_mult()
