import functools

@functools.cache
def distance (seq1, seq2):
    #levenshtein distance

    #base cases
    if len(seq1) == 0:
        return len(seq2)
    elif len(seq2) == 0:
        return len(seq1)

    if seq1[0] == seq2[0]:
        return distance(seq1[1:], seq2[1:])
    else:
        return 1 + min((
            distance(seq1[1:], seq2),
            distance(seq1, seq2[1:]),
            distance(seq1[1:], seq2[1:])
        ))
