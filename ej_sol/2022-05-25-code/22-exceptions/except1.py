'''
Exceptions v1: Basic usage of try and except
'''

# -----------------------------------------------------------------------------
def check_seq(seq: str, allowed_letters: list[str]):

    checks: list[bool] = [(letter in allowed_letters) for letter in seq]
    all_ok: bool       = all(checks)

    if not all_ok:
        raise Exception('The sequence has incorrect bases!')

# -----------------------------------------------------------------------------
if __name__ == '__main__':

    DNA_LETTERS:  list[str] = list("ATCG")
    seq_list:     list[str] = ['ATCG', 'ATXX', 'GATA']
    correct_seqs: list[str] = []

    for seq in seq_list:
        try:
            check_seq(seq, DNA_LETTERS)
            correct_seqs.append(seq)
        except:
            print(f'{seq} is an incorrect sequence. Skipping it...')
    
    print(f'Checked sequences: {correct_seqs}')

# -----------------------------------------------------------------------------
