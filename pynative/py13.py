def get_factorial():
    a: int = int(input("de que numero busco el factorial : "))
    b: int = 1
    finished: bool = (a < 1)

    while not finished:
        b = b * a
        a = a - 1
        finished = (a < 1)
    print(b)
get_factorial()