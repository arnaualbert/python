from pathlib import Path
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

        raw_text:       str             = Path(fasta_path).read_text()

        # Split in lines
        fasta_lines: list[str] = raw_text.split("\n")

        # Remove comment line (first line)
        del fasta_lines[0]

        # Join all lines
        dna: str = "".join(fasta_lines)
        
        sequencia = cls(dna)

        assert len(sequencia) == 8

        return sequencia

sequencia = Seq.from_fasta('data_dna.fasta')
print(sequencia)
