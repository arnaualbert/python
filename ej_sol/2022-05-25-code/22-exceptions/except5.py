'''
Exceptions v5: Check DNA sequence
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
    except:
        print('Ha habido un error con la secuencia:')


# -----------------------------------------------------------------------------
