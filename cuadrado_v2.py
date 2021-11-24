class Square:
    x:     float
    y:     float
    lenght:float

    def __init__(self, x: float, y: float, lenght: float):
        "Constructor"

        self.x = x
        self.y = y
        self.lenght = lenght

    def get_upper_left_x(self) ->float :
        "la x del vertice superior izquierdo es "
        
        midlenght: float = self.lenght/2

        upper_left_x = self.x - midlenght
        upper_left_y = self.y + midlenght
        result = upper_left_x
        return result

    def get_upper_left_y(self) ->float :
        "la x del vertice superior izquierdo es "
        
        midlenght: float = self.lenght/2

        upper_left_x = self.x - midlenght
        upper_left_y = self.y + midlenght
        result = upper_left_y
        return result

    def get_upper_right_x(self) ->float :
        "la x del vertice superior izquierdo es "
        
        midlenght: float = self.lenght/2

        upper_right_x = self.x - midlenght
        upper_right_y = self.y + midlenght
        result = upper_right_x
        return result

    def get_upper_right_y(self) ->float :
        "la x del vertice superior izquierdo es "
        
        midlenght: float = self.lenght/2

        upper_right_x = self.x - midlenght
        upper_right_y = self.y + midlenght
        result = upper_right_y
        return result

s: Square = Square(0,0,10)

print("Atributos de el quadrado s: ")
print(s.x)
print(s.y)
print(s.lenght)

print("vertice superior izquierdo de el cuadrado s: ")
print(s.get_upper_left_x())
print(s.get_upper_left_y())

print("vertice superior derecho de el cuadrado s: ")
print(s.get_upper_right_x())
print(s.get_upper_right_y())