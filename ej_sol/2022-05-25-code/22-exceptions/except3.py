'''
Exceptions v3: With... example. Equivalent to v2.
'''

# -----------------------------------------------------------------------------
def except3():

    seq: str = 'ATCG'
    dna_file = open('dna_seq.txt', 'w')

    with open('dna_seq.txt', 'w') as dna_file:

        for letter in seq:
            dna_file.write(letter)


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    except3()

# -----------------------------------------------------------------------------
