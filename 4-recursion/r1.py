




#--------------------------------------------------------------------------------------------------
def say_hello_v1():

    while True:
        print("Hello")
        
#--------------------------------------------------------------------------------------------------
def say_hello_v2():

    print("Hello")
    say_hello_v2()

#--------------------------------------------------------------------------------------------------
def say_hello_v3():

    for _ in range(5):
        print("Hello")

#--------------------------------------------------------------------------------------------------
def say_hello_v4(num_veces: int):
    num_veces: int = num_veces - 1
    print("Hello")
    if num_veces > 0:
        say_hello_v4(num_veces)

#--------------------------------------------------------------------------------------------------
def say_hello_v5(num_veces: int):
    print("Hello")
    num_veces: int
    if num_veces > 0:
        say_hello_v4(num_veces - 1)

#--------------------------------------------------------------------------------------------------
def say_hello_oficial_v1(num: int):

    if (num > 0):
        print("Hello")
        say_hello_oficial_v1(num - 1)

    if (num == 0):
        print("Finished!")

#--------------------------------------------------------------------------------------------------
def say_hello_oficial_v2(num: int):

    if (num > 0):
        print("Hello")
        say_hello_oficial_v2(num - 1)

    if (num <= 0):
        print("Finished!")    

#--------------------------------------------------------------------------------------------------
# NO TAN RECOMENDABLE
def say_hello_oficial_v2_2(num: int):

    if (num > 0):
        print("Hello")
        say_hello_oficial_v2_2(num - 1)

    else:
        print("Finished!")    

#--------------------------------------------------------------------------------------------------
def say_hello_oficial_v2_3(num: int):

    if (num > 0):
        print("Hello")
        say_hello_oficial_v2_3(num - 1)

    elif (num <= 0):
        pass
# Main

#--------------------------------------------------------------------------------------------------

say_hello_oficial_v2(5)

#--------------------------------------------------------------------------------------------------

