import levenshtein_distance_algorithm
import soundex_convert_algorithm
import jaro_similarity_algorithm
import double_metaphone_algorithm
from read_data import first_name
from test import soundex_first_name_only, soundex_first_fathers_name, \
    levenshtein_first_fathers_name, test_levenshtein_first_name_only, \
    jaro_first_name_only, jaro_first_fathers_name, \
    dmetaphone_test_first_name_only, dmetaphone_test_first_fathers_name, \
    jw_similarity_first_names_only, jw_similarity_first_fathers_names
from blocking_rules import rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, \
    rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule8_1, rule8_2, rule22, rule23, rule24
from jaro_similarity_algorithm import jaro_sim
# from jaro_winkler_java_algorithm import jaro_sim
from time import time


def main():
    small_data = "/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/data-01000-00500-abcd.csv"
    medium_data = "/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/data-10000-05000-abcd.csv"

    rule8(small_data)


def full_test():
    directories = ["data-00100-00050-abcd.csv",
                   "data-00200-00100-abcd.csv",
                   "data-01000-00500-abcd.csv",
                   "data-02000-01000-abcd.csv",
                   "data-10000-05000-abcd.csv",
                   "data-30000-15000-abcd.csv"]

    for file_name in directories:
        print(file_name)
        t1 = time()
        soundex_first_fathers_name("/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/" + file_name)
        t2 = time()
        print()
        print("SoundEx, first and father's name", t2 - t1)
        print()
        soundex_first_name_only("/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/" + file_name)
        t3 = time()
        print()
        print("SoundEx, first name only", t3 - t2)
        print()
        test_levenshtein_first_name_only("/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/" + file_name)
        t4 = time()
        print()
        print("Levenshtein, first name only", t4 - t3)
        print()
        levenshtein_first_fathers_name("/home/bruce/Documents/tools/data-generator/GECO-Ethiopia/" + file_name)
        t5 = time()
        print()
        print("Levenshtein, first and father's name", t5 - t4)
        print()


if __name__ == '__main__':
    s = time()
    main()
    e = time()
    print(e - s)
