count : int = -11
finished : bool = (count > -2)
while not finished:
    count = count + 1
    print(count)
    finished = (count > -2)
print("DONE!")