def tokenize(
        nucleotide_sequence):
    """
    tokenize converts a nucleotide sequence to a sequence of ids.

    nucleotide_sequence -- DNA sequence string consisting of A, C, G, T
    return -- a x-length array consisting of ints corresponding to nucleotides (positions to be decided later)
    """ 
    mappings = {
        "A" : 0,
        "C" : 1,
        "G" : 2,
        "T" : 3
    } # Declares the integers that correspond to each nucleotide
    arr = [mappings[x] for x in nucleotide_sequence] # Converts nucleotide array to array of ints based on mappings
    return arr

def tokenize_k(
        nucleotide_sequence,
        k):
    """
    tokenize_k converts a nucleotide sequence to a list of encoded k-mers.

    nucleotide_sequence -- DNA sequence string consisting of A, C, G, T
    k -- the length of the k-mers
    return -- a list of int lists corresponding to k-mers (positions to be decided later)
    """ 
    mappings = {
        "A" : 0,
        "C" : 1,
        "G" : 2,
        "T" : 3
    } # Declares the integers that correspond to each nucleotide
    num_kmers = len(nucleotide_sequence) - k + 1 # Declares the number of kmers based on k and length of sequence
    kmer_list = [] # Declares an empty list
    for x in range(0, num_kmers):
        kmer = nucleotide_sequence[x:x+k] # Creates a slice of the nucleotide sequence string
        kmer_list.append([mappings[y] for y in kmer]) # Converts the slice into an array of ints, and adds it to the empty list
    return kmer_list
