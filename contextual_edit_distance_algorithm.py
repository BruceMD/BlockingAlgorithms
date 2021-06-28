

def context_distance(seq1, seq2):
    dist = 0

    for i in range(len(seq1) + 1):
        for j in range(len(seq2) + 1):
            for k in range(len(seq1) + len(seq2) + 1):
                pass
