'''
Exceptions v6: Capturing Exception objects
'''

# -----------------------------------------------------------------------------
def get_seq():
    seq: str = input('Escribe una secuencia de ADN: ')

    len_is_ok: bool = ((len(seq) % 3) == 0)

    if not len_is_ok:
        raise Exception('Error: Seq with incomplete codon at the end.')

    return seq

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        seq: str = get_seq()
        print(f'La secuencia es {seq}')
    except Exception as excpt:
        print('Ha habido un error con la secuencia:')
        print(excpt)
    except KeyboardInterrupt as excpt:
        print('Has abortado en medio de escribir la secuencia. Acábala por favor.')



# -----------------------------------------------------------------------------
