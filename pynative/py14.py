num = 76542
reverse_number = 0
print("Di un numero: ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Numero de el reves: ", reverse_number)