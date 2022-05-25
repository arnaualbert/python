'''
Exceptions v4: Check int
'''

# -----------------------------------------------------------------------------
def check_int():
    num_str: str = input('Escribe un entero: ')
    num:     int = int(num_str)
    return num

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        num: int = check_int()
        print(f'Has escrito {num}')
    except:
        print('Ha habido un error con tu número. Vuelve a escribirlo.')

# -----------------------------------------------------------------------------
