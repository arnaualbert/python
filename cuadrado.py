from turtle import *
setup(500,500,0,0)
def get_upper_left_x(x:float,
                    y:float,
                    lenght:float) -> float:
    
    
    midlenght: float = lenght/2

    upper_left_x = x - midlenght
    upper_left_y = y + midlenght
    result = upper_left_x
    return result