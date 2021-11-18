import pprint

# Lists

# list literals
l1: list = [] # lista vacia
l2: list[str] = ["John", "Mel", "Lucy"] # Los subtipos van entre []

# lenght of a list
l2_len: int = len(l2)

# element acces

print(l2[0]) #John
print(l2[2])  #Lucy
print(l2[-1])   #Lucy
print(l2[len(l2)-1]) #Lucy

l2[2][0] # "Lucy"[0]

# sublistas

l3: list[str] = ["a", "b", "c", "d", "e", "f"]
print(l3[0:4]) # a,b,c,d
print(l3[4:6]) # e,f
print(l3[4:]) # e,f

# list operation
print(["John", "Mary", "Lucy"]+["Peter", "Isaac"])
print([1,2,3] * 3) #repite elementos

# multiple types in a list not recomended
l4:list[object] = print([1,"John", True,0.9])
l5:list[list[int]] = [[1,2],[3,4]]

first_row = l5[0]
second_row = l5[1]
print(f"{first_row}\n{second_row}")
#⨪----------------------------------------------------------------------------------------------------------------------

# assignment List are mutable

l3[0] = "z" #cambia la letra en posicion 0 por z 
l3[0] = "a"
print(l3)

# slice assignment

l3[3:] = [1,2,3] # d,e,f por 1,2,3
l3[3:] = ["d"] # new assigment can be different lenghts
l3[3:] = [] # borras lo que hay apartir de el num
l3 = [] # borra todo
l3[:] = [] #borra todo
print(l3)



# prints
print(l2_len)

print(l1)
print(len(l2))