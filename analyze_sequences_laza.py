# analyze_sequences.py Notes
# Lazarina Butkovich 6/5/25

# Open Bootcamp Collective (OBC) HW 1: https://github.com/open-bootcamp-collective/bioinformatics-cohort-1/blob/main/01-Intro_to_coding/group_homework_1.md

"""
Setup Notes
"""
# Conda Notes: 
#   - created and activated a new conda environment with Python 3.10.
#   - Did this by using the Ctrl+Shift+P command in VS Code, then typing ">Python: Create Environment", selecting "Conda", and selecting the Python 3.10 interpreter.
#   - Can check Python version by typing "python" or "python --version" in the terminal.

# Biopython Notes 
#   - Installed Biopython using the command "pip install biopython" in the terminal.


from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

"""
Functions
"""
def gc_content(seq):
    """Computes GC content of a sequence.

    Args:
        seq: str, DNA sequence.

    Returns:
        float, GC content as a percentage.    
    """
    return gc_fraction(Seq(seq))

def is_valid(seq):
    """Checks if a sequence is valid (contains only A, T, C, G).

    Args:
        seq: str, DNA sequence.

    Returns:
        bool, True if valid, False otherwise.
    """
    return all(base in 'ATCG' for base in seq)

"""
Main
"""
dna_list = ['ATGCGTACG', 'ATCGTACG', 'ATGCGTACGTAGC', 'ATCGTACGTAGC', 'ATGCGTACGTAGCTAGC', 'dinosaurs are cool']

for dna in dna_list:
    print(f"Sequence: {dna}")
    print(f"Length: {len(dna)} nt")
    print(f"GC Content: {gc_content(dna):.2%}")
    print(f"Valid DNA Sequence?: {is_valid(dna)}")
    print(f"Reverse Complement: {Seq(dna).reverse_complement()}")
