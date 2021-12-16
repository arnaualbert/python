from pathlib import Path
import re
from typing import Pattern

# -----------------------------------------------------------------------------
# Student name: Arnau Albert Sanchez
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Q3: get_indexes()
# - Input:
#   - target: str. A string of nucleotides we want to search.
#   - fasta:  str. The contents of a fasta file.
# - Output:
#   - indexes: list[int] with all indexes where we found the target.
# 
# - Notes:
#   - Fasta files are very common in Bioinformatics.
#     The first line is always a comment and the other lines form a sequence.
#   - Indexes start at 0, the usual in Python.
#   - get_indexes() returns an empty list if the target cannot be found.
#   - get_indexes() returns all indexes it finds.
#   - get_indexes() also finds overlapping targets.
# 
# - Remember:
#   - Write your solution inside the given function.
#   - Functions must be pure. Remember to delete your print() calls when done.
#   - You can write additional functions to simplify your algorithm.
# -----------------------------------------------------------------------------


# - Write your solution here.
# - This function must be pure. Remember to delete your print() calls when done.
# -----------------------------------------------------------------------------
def get_indexes(target: str, fasta: str) -> list[int]:

    lines: str = fasta.split("\n")
    del lines[0]

    dna: str = "".join(lines)
    
    indexes: list[int] = []

    for index in range(len(dna)):
        dna_sol: bool = dna.startswith(target, index)
        if dna_sol == True:
            indexes.append(index)
    return indexes


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    # Write your solution inside the function.
    # Code here is not evaluated.
    # This is just for your convenience.
    coronavirus_fasta: str = Path("q3_coronavirus.fasta").read_text()
    print(get_indexes("AAA", coronavirus_fasta))

# -----------------------------------------------------------------------------
