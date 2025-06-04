dna_sequences = [
    "ATGCGTACCTGA",
    "TACGGTAGCTAA",
    "GGCTAACCGTTA",
    "CCTGAGGCTTAC",
    "AATCGGTANCXT"  
]

# Function to calculate GC content
def gc_content(seq):
    return ((seq.count("G") + seq.count("C")) / len(seq)) * 100

# Function to check if a sequence is valid (only A, T, C, G)
def is_valid(seq):
    return all(base in "ATCG" for base in seq)

# Loop to analyze each sequence
for i, seq in enumerate(dna_sequences, 1):
    length = len(seq)
    gc = gc_content(seq)
    valid = is_valid(seq)
    
    print(f"Sequence {i}: {seq}")
    print(f"  Length: {length}")
    print(f"  GC Content: {gc:.2f}%")
    print(f"  Valid: {'Yes' if valid else 'No'}")
    print("-" * 40)
