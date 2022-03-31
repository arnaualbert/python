'''
Object oriented programing
'''

# Clases empiezan en mayusculas

class BadExample():
    pass

# Las clases tienen un constructor
#on definition we write __init__ ()
#on callinf we called Dog
#methods :
#all methods have a special parameter: self
#when calling the method we don't write it
#attributes:
#attributes are variables stores inside the objects
#they are created by the constructor 
#to access them write self.<attribute>
#-----------------------------------------------------
class Dog():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

#----------------------------------------------------
firulas: Dog = Dog("firulais",3)
print(firulas.name)
print(firulas.age)
