
def get_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    lista = {}

    for i in range(len(keys)):
        lista.update({keys[i]:values[i]})

