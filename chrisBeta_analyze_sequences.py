from Bio.Seq import Seq

seq1 = Seq("AGTACACTGGT")
seq2 = Seq("AGTAAACTGGT")
seq3 = Seq("AGTACACTAAT")
seq4 = Seq("CGTACACTGGT")
seq5 = Seq("AGTGGGGXGGT")
seq_list = ["seq1","seq2","seq3","seq4","seq5"]

def gc_content(seq):
    if len(seq) == 0:
        return 0.0  # Handle empty sequences to avoid division by zero  
    else:          
        return ((seq.count("G") + seq.count("C")) / len(seq)) * 100

def is_valid(seq):
    return all(base in "ATCG" for base in seq)

for seq in seq_list:
    print(f"Sequence: {seq}")
    print(f"Length: {len(seq)} nt")
    print(f"GC Content: {gc_content(seq):.2%}")
    print(f"Valid DNA Sequence?: {is_valid(seq)}")
    print(f"Reverse Complement: {Seq(seq).reverse_complement()}")