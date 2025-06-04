# analyze_sequences.py Notes

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
