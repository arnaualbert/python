'''
Exceptions v2: Try and except with files
'''

# -----------------------------------------------------------------------------
def except2():

    seq: str = 'ATCG'
    dna_file = open('dna_seq.txt', 'w')

    try:
        for letter in seq:
            dna_file.write(letter)
    except:
        dna_file.close()

# -----------------------------------------------------------------------------
if __name__ == '__main__':
    except2()

# -----------------------------------------------------------------------------
