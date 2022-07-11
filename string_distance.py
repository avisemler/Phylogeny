import functools

@functools.cache
def distance (seq1, seq2):
    #levenshtein distance

    m = len(seq1)
    n = len(seq2)
    matrix = np.zeros((m + 1, n + 1))

    for i in range(m):
        #The distance between the a prefix and the empty string is the length
        matrix[i + 1, 0] = i + 1

    for j in range(n):
        matrix[0, j + 1] = j + 1

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            print(i,j)
            if seq1[i - 1] == seq2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i, j] = min([
                matrix[i - 1, j] + 1,
                matrix[i, j - 1] + 1,
                matrix[i - 1, j - 1] + cost,
            ])
            
    return matrix[m, n]
