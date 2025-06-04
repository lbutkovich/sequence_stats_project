from Bio.Seq import Seq

seq1 = Seq("AGTACACTGGT")
seq2 = Seq("AGTAAACTGGT")
seq3 = Seq("AGTACACTAAT")
seq4 = Seq("CGTACACTGGT")
seq5 = Seq("AGTGGGGGGGT")
sequences = ["seq1","seq2","seq3","seq4","seq5"]

def gc_content:

    gc_count = sequence.count('G') + sequence.count('C')
        total_bases = len(sequence)

        if total_bases == 0:
            return 0.0  # Handle empty sequences to avoid division by zero

    gc_percentage = (gc_count / total_bases) * 100
    return gc_percentage