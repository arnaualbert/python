def get_digitnum():
    num = 75869
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1
    print( count)

get_digitnum()