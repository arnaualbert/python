def get_upper_left_x(x:float,
                    y:float,
                    lenght:float) -> float:
    
    
    midlenght: float = lenght/2

    upper_left_x = x - midlenght
    upper_left_y = y + midlenght
    result = upper_left_x
    return result

x = 0
y = 0
lenght = 10
upper_left_x = get_upper_left_x(x,y,lenght)
print("la x del vertice superior izquierdo es ")
print(upper_left_x)

def get_upper_left_y(x:float,
                    y:float,
                    lenght:float) -> float:
    
    
    midlenght: float = lenght/2

    upper_left_x = x - midlenght
    upper_left_y = y + midlenght
    result = upper_left_y
    return result

x = 0
y = 0
lenght = 10
upper_left_y = get_upper_left_y(x,y,lenght)
print("la y del vertice superior derecho es ")
print(upper_left_y)

def get_upper_right_x(x:float,
                    y:float,
                    lenght:float) -> float:
    
    
    midlenght: float = lenght/2

    upper_right_x = x - midlenght
    upper_right_y = y + midlenght
    result = upper_right_x
    return result

x = 0
y = 0
lenght = 10
upper_right_x = get_upper_right_x(x,y,lenght)
print("la x del vertice inferior izquierdo es ")
print(upper_right_x)

def get_upper_right_y(x:float,
                    y:float,
                    lenght:float) -> float:
    
    
    midlenght: float = lenght/2

    upper_right_x = x - midlenght
    upper_right_y = y + midlenght
    result = upper_right_y
    return result

x = 0
y = 0
lenght = 10
upper_right_y = get_upper_right_y(x,y,lenght)
print("la y del vertice inferior derecho es ")
print(upper_right_y)