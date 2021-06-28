from math import floor
from jaro_similarity_algorithm import jaro_sim


def jw_similarity(name1, name2):
    js = jaro_sim(name1, name2)

    prefix = 0
    for i in range(min(len(name1), len(name2))):
        if name1[i] == name2[i]:
            prefix += 1
        else:
            break

    prefix = min(4, prefix)

    return js + 0.1 * prefix * (1 - js)

