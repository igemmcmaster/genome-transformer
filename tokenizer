def tokenize(
        nucleotide_sequence):
    """
    tokenizer converts a nucleotide sequence to a sequence of ids.

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
