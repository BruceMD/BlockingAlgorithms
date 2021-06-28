import math


def jaro_sim(name1, name2):

    mtp = matches(name1, name2)
    m = mtp[0]
    if m == 0:
        return 0
    j = (m / len(name1) + m/len(name2) + (m - mtp[1]) / m) / 3


def matches(name1, name2):

    if len(name1) > len(name2):
        max_name = name1
        min_name = name2
    else:
        max_name = name2
        min_name = name1

    range_transposition = math.floor(max(len(max_name) / 2 - 1, 0))
    match_indexes = [-1 for _ in range(len(min_name))]
    match_flags = [False for _ in range(len(max_name))]
    matching_values = 0

    for m in range(len(min_name)):
        char = min_name[m]
        n = max(m - range_transposition, 0)
        upper_limit = min(m + range_transposition + 1, len(max_name))
        while n < upper_limit:
            if not match_flags[n] and char == max_name[n]:
                match_flags[m] = True
                match_indexes[m] = n
                matching_values += 1
                break
            n += 1

    print(match_flags)
    print(match_indexes)

    ms1, ms2 = [], []
    i, si = 0, 0
    while i < len(min_name):
        if match_indexes[i] != -1:
            ms1[si] = min_name[i]
            si += 1
        i += 1

    i, si = 0, 0
    while i < len(max_name):
        if match_flags[i]:
            ms2[si] = max_name[i]
            si += 1
        i += 1

    trans = 0
    for m in range(len(ms1)):
        if ms1[m] != ms2[m]:
            trans += 1

    prefix = 0
    for m in range(len(min_name)):
        if name1[m] != name2[m]:
            prefix += 1

    print(matching_values, trans / 2, prefix, len(max_name))
    return [matching_values, trans / 2, prefix, len(max_name)]
