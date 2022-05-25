from pathlib import Path

# GLOBAL CONSTANTS
# -----------------------------------------------------------------------------
DNA_LETTERS: list[str] = list("ATCG")
RNA_LETTERS: list[str] = list("AUCG")
AA_LETTERS:  list[str] = list("ARNDCEQGHILKMFPSTWYV")
AMINO:  dict[str, str] = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"*", "UAG":"*",
    "UGU":"C", "UGC":"C", "UGA":"*", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",
}

# -----------------------------------------------------------------------------
def read_fasta(filename: str) -> str:

    fasta_path: Path = Path(filename)
    txt:        str  = fasta_path.read_text()

    lines:  list[str] = txt.strip().splitlines()
    header: str       = lines[0]
    body:   list[str] = lines[1:]

    seq: str = ''.join(body)

    return seq


# -----------------------------------------------------------------------------
def check_seq(seq: str, allowed_letters: list[str]) -> bool:

    check_letter: function = lambda letter: (letter in allowed_letters)

    checks: list[bool] = [check_letter(letter) for letter in seq]
    result: bool       = all(checks)

    return result


# -----------------------------------------------------------------------------
def translate(seq: str) -> str:

    assert (len(seq) % 3) == 0, 'Sequence is not multiple of three. Has an incomplete codon.'

    start_list: list[int] = list(range(0, len(seq), 3))
    end_list:   list[int] = [ start+3 for start in start_list ]

    codon_list: list[str] = [ seq[start:end]
                              for start, end
                              in zip(start_list, end_list) ]

    aa_list: list[str] = [ AMINO[codon] for codon in codon_list ]
    protein: str       = ''.join(aa_list)

    return protein


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    pass
    # Write your solution in functions.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
