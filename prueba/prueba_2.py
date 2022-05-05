from pathlib import Path
from re import S
import utils


# Student name: WRITE YOUR NAME BELOW
# -----------------------------------------------------------------------------
name:    str = "Arnau"
surname: str = "Albert"
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
# WRITE YOUR CODE HERE

class Seq:
    
    def __init__(self,seq: str) -> None:
        self.seq = seq

    def __str__(self) -> str:
        
        sequencia = self.seq
        return sequencia
    
    def __len__(self):

        return len(self.seq)

    @classmethod
    def from_fasta(cls,fasta_path: Path):

        raw_text:str = Path(fasta_path).read_text()

        # Split in lines
        fasta_lines: list[str] = raw_text.split("\n")

        # Remove comment line (first line)
        del fasta_lines[0]

        # Join all lines
        dna: str = "".join(fasta_lines)
        
        sequencia = dna

        return sequencia



class Protein(Seq):

    def __init__(self, seq: str) -> None:
        super().__init__(seq)

class RNASeq(Seq):
    
    def __init__(self, seq: str) -> None:
        super().__init__(seq)


class DNASeq(Seq):
    
    def __init__(self, seq: str) -> None:
        super().__init__(seq)

    def get_transcription(self):

        transcription = self.seq.replace('T','U')

        return transcription


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    s: DNASeq = DNASeq('ATCG')
    
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
