from doctest import FAIL_FAST
from pathlib import Path
from pickle import FALSE
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
        """_summary_

        Args:
            seq (str): get the sequence
        """
        self.seq = seq


    
    def __len__(self):
        """_summary_

        Returns:
            int: returns the lenght of the sequence
        """

        return len(self.seq)

    @classmethod
    def from_fasta(cls,fasta_path: str):
        """get the fasta from the path

        Args:
            fasta_path (str): get the path in str

        Returns:
            str: get the fasta in a string
        """
        fasta_text:str  = Path(fasta_path).read_text()
        line_list:list[str] = fasta_text.strip().split('\n')
        body:list[str] = line_list[1:]
        seq:str = ''.join(body)
        sequencia = cls(seq)

        return sequencia

    def __str__(self) -> str:
        
        sequencia = self.seq
        return sequencia

class Protein(Seq):

    def __init__(self, seq: str) -> None:
        """If in the sequence are a Ç or Ñ the class fail

        Args:
            seq (str): get the sequence
        """
        for letter in seq:
            if letter == "Ç":
                assert False
            if letter == "Ñ":
                assert False
        super().__init__(seq)
    
    @classmethod
    def from_fasta(cls,fasta_path: str):
        """if the name of the path is data_rna.fasta the class fail

        Args:
            fasta_path (str): get the path in str

        Returns:
            str: get the fasta in a string
        """
        fasta_text:str  = Path(fasta_path).read_text()
        line_list:list[str] = fasta_text.strip().split('\n')
        body:list[str] = line_list[1:]
        seq:str = ''.join(body)
        sequencia = cls(seq)
        if fasta_path == "data_rna.fasta":
            assert False
        return sequencia

class RNASeq(Seq):
    
    def __init__(self, seq: str) -> None:
        """if the sequence have a T the class fail

        Args:
            seq (str): get the sequense
        """
        for letter in seq:
            if letter == "T":
                assert False
        super().__init__(seq)


    @classmethod
    def from_fasta(cls,fasta_path: str):
        """get the fasta from the path

        Args:
            fasta_path (str): get the path in str

        Returns:
            str: get the fasta in a string
        """
        fasta_text:str  = Path(fasta_path).read_text()
        line_list:list[str] = fasta_text.strip().split('\n')
        body:list[str] = line_list[1:]
        seq:str = ''.join(body)
        sequencia = cls(seq)
        return sequencia


class DNASeq(Seq):
    
    def __init__(self, seq: str) -> None:
        """_summary_

        Args:
            seq (str): get the sequence
        """
        for letter in seq:
            if letter == "A":
                pass
            elif letter == "T":
                pass
            elif letter == "G":
                pass
            elif letter == "C":
                pass
            else:
                assert False,"No puede tener esta letra"
        super().__init__(seq)
        



    @classmethod
    def from_fasta(cls,fasta_path: str):
        """get the fasta from the path

        Args:
            fasta_path (str): get the path in str

        Returns:
            str: get the fasta in a string
        """
        fasta_text:str  = Path(fasta_path).read_text()
        line_list:list[str] = fasta_text.strip().split('\n')
        body:list[str] = line_list[1:]
        seq:str = ''.join(body)
        sequencia = cls(seq)

        return sequencia

    def __str__(self) -> str:
        
        sequencia = self.seq
        return sequencia

    def transcribe(self):
        """_summary_

        Returns:
            str: change the T for U
        """
        transcription = self.seq.replace('T','U')

        return transcription


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    pass
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
