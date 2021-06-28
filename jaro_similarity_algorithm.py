from math import floor, ceil


def jaro_sim(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    if len(name1)*len(name2) == 0:
        return 0
    if name1 == name2:
        return 1
    len1, len2 = len(name1), len(name2)
    max_dist = floor(max(len1, len2) / 2) - 1
    match = 0
    hash_name1 = [0] * len(name1)
    hash_name2 = [0] * len(name2)
    for i in range(len1):
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):
            if name1[i] == name2[j] and hash_name2[j] == 0:
                hash_name1[i] = 1
                hash_name2[j] = 1
                match += 1
                break
    if match == 0:
        return 0

    common1, common2 = [], []
    for num, boo in enumerate(hash_name1):
        if boo:
            common1.append(name1[num])
    for num, boo in enumerate(hash_name2):
        if boo:
            common2.append(name2[num])

    transpositions = 0
    for i in range(len(common1)):
        if common1[i] != common2[i]:
            transpositions += 1
    transpositions /= 2

    return (match / len1 + match / len2 + (match - transpositions) / match) / 3.0