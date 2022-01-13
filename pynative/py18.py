# num:int = 5
# row: int= 0
# finished: bool = (row < num)
# star: int = 0
# finished2: bool = (star > 0)
# while not finished:
#     star = row + 1
#     while not finished2:
#         print("*")
#         star = star - 1
#     row = row + 1
#     print()

n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = 1
    while j <= i:
        print("*", end = " ")
        j += 1
    print()
    i += 1
i = 1
while i <= n :
    j = n
    while j >= i:
        print("*", end = " ")
        j -= 1
    print()
    i += 1