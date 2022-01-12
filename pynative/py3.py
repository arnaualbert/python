
a : int = 0
f: int = int(input("pon un numero: "))
finished : bool = (a < f)

while not finished:
    a = (a + 1)
    print(a)
    finished = (a < f)
