from Bio.Seq import Seq

def gc_content(seq):
    if len(seq) == 0:
        return 0.0  # Handle empty sequences to avoid division by zero  
    else:          
        return ((seq.count("G") + seq.count("C")) / len(seq))

def is_valid(seq):
    return all(base in "ATCG" for base in seq)

seq1 = "AGTACACTGGT"
seq2 = "AGTAAACTGGT"
seq3 = "AGTACACTAAT"
seq4 = "CGTACACTGGT"
seq5 = "AGTGGGGXGGT"
seq_list = [seq1, seq2, seq3, seq4, seq5]

for seq in seq_list:
    print(f"Sequence: {seq}")
    print(f"Length: {len(seq)} nt")
    print(f"GC Content: {gc_content(seq):.2%}")
    print(f"Valid DNA Sequence?: {is_valid(seq)}")
    print(f"Reverse Complement: {Seq(seq).reverse_complement()}")