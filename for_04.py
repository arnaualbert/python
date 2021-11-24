import pprint
import random
import copy

#-------------------------------------------------------------------------------------------------------------------------------------

# pedir tres numeros con input , recorrerlos y sumarlos

# ej5

nums: list[int] = []
sumnums = 0

print("Escribe el primer numero : ")
num1: int = int(input())
nums.append(num1)
print("Escribe el segundo numero : ")
num2: int = int(input())
nums.append(num2)
print("Escribe el tercer numero : ")
num3: int = int(input())
nums.append(num3)

for number in nums:
    sumnums += number

print(sumnums)