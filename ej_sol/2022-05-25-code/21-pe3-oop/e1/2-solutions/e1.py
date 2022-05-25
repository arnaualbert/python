import utils


# Student name: WRITE YOUR NAME BELOW
# -----------------------------------------------------------------------------
name:    str = "XXX"
surname: str = "XXX"
assert name and surname, 'Error: Please write your name and surname.'
# -----------------------------------------------------------------------------

# E1
# -----------------------------------------------------------------------------
# 1. Fes quatre classes: Seq, DNASeq, RNASeq, Protein.
# 2. DNASeq, RNASeq i Protein han d'heretar de Seq.
# 3. Codifica els atributs i els mètodes necessaris per tal que
#   passin tots els tests que hi ha a l'arxiu 'e1_test.py'.
# 4. Executeu els tests amb l'ordre: pytest -v
# 5. A l'arxiu 'utils.py' teniu codi que us pot ajudar.
# 6. Tot el codi ha d'estar a les classes o a utils.py.
# 7. En cap cas poseu codi a la secció Main. Us donarà problemes en executar pytest.
# -----------------------------------------------------------------------------


# Classes
# -----------------------------------------------------------------------------
class Seq:

    def __init__(self, seq: str):
        self.seq = seq
    
    @classmethod
    def from_fasta(cls, filename: str):
        seq: str = utils.read_fasta(filename)
        return cls(seq)
    
    def __str__(self) -> str:
        return self.seq

    def __len__(self) -> int:
        return len(self.seq)


# -----------------------------------------------------------------------------
class Protein(Seq):

    def __init__(self, seq: str):
        super().__init__(seq)
        assert utils.check_seq(self.seq, utils.AA_LETTERS)


# -----------------------------------------------------------------------------
class RNASeq(Seq):

    def __init__(self, seq: str):
        super().__init__(seq)
        assert utils.check_seq(self.seq, utils.RNA_LETTERS)
    
    def translate(self) -> str:
        aa_str: str = utils.translate(self.seq)
        return aa_str


# -----------------------------------------------------------------------------
class DNASeq(Seq):

    def __init__(self, seq: str):
        super().__init__(seq)
        assert utils.check_seq(self.seq, utils.DNA_LETTERS)
    
    def transcribe(self) -> str:
        rna_str: str = self.seq.replace('T', 'U')
        return rna_str


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    pass
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
