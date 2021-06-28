from phonetics import dmetaphone, soundex


def mod_dmetaphone(name):

    d_tuple = dmetaphone(name)

    return d_tuple[0], d_tuple[1]
#    return d_tuple[0][0:4], d_tuple[1][0:4]

    # reducing the dmetaphone output to 4 characters broadens the range of acceptability
    # this reduces the FNs from 57 -> 41


def compare_dmetaphone(output1, output2):

    for t in output1:
        if t in output2 and len(t) > 0:
            return True
    return False
