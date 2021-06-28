from read_data import first_name, fathers_name, identity_number, town_name, case_number, dob, phone_number
from double_metaphone_algorithm import compare_dmetaphone, mod_dmetaphone
from soundex_convert_algorithm import convert_to_soundex
from jaro_winkler_similarity_algorithm import jaro_sim
from levenshtein_distance_algorithm import edit_distance
from fastDamerauLevenshtein import damerauLevenshtein as dlev
from Levenshtein import distance
from damerau_levenshtein import damerau_levenshtein_distance_improved as dld


def rps(bool1, bool2, bool3):
    return (bool1 and bool2) or (bool1 and bool3) or (bool2 and bool3)


def count_triangle(num):
    count = 0
    for i in range(num):
        count += i
    return count


def rule1(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(compare_dmetaphone(mod_dmetaphone(names_list[i]), mod_dmetaphone(names_list[j])),
                   compare_dmetaphone(mod_dmetaphone(fathers_names_list[i]), mod_dmetaphone(fathers_names_list[j])),
                   compare_dmetaphone(mod_dmetaphone(town_list[i]), mod_dmetaphone(town_list[j]))):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule ONE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule2(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                   convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                   convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWO \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule3(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                   convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                   convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(compare_dmetaphone(mod_dmetaphone(names_list[i]), mod_dmetaphone(names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(fathers_names_list[i]), mod_dmetaphone(fathers_names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(town_list[i]), mod_dmetaphone(town_list[j]))):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule THREE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule4(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(jaro_sim(names_list[i], names_list[j]) > 0.85,
                   jaro_sim(fathers_names_list[i], fathers_names_list[j]) > 0.85,
                   jaro_sim(town_list[i], town_list[j]) > 0.85):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule FOUR \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule5(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                   convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                   convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(compare_dmetaphone(mod_dmetaphone(names_list[i]), mod_dmetaphone(names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(fathers_names_list[i]), mod_dmetaphone(fathers_names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(town_list[i]), mod_dmetaphone(town_list[j]))):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(jaro_sim(names_list[i], names_list[j]) > 0.75,
                     jaro_sim(fathers_names_list[i], fathers_names_list[j]) > 0.75,
                     jaro_sim(town_list[i], town_list[j]) > 0.75):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule FIVE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule6(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                   convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                   convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(compare_dmetaphone(mod_dmetaphone(names_list[i]), mod_dmetaphone(names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(fathers_names_list[i]), mod_dmetaphone(fathers_names_list[j])),
                     compare_dmetaphone(mod_dmetaphone(town_list[i]), mod_dmetaphone(town_list[j]))):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(jaro_sim(names_list[i], names_list[j]) > 0.65,
                     jaro_sim(fathers_names_list[i], fathers_names_list[j]) > 0.65,
                     jaro_sim(town_list[i], town_list[j]) > 0.65):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule SIX \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule7(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(distance(names_list[i], names_list[j]) <= 2,
                   distance(fathers_names_list[i], fathers_names_list[j]) <= 2,
                   distance(town_list[i], town_list[j]) <= 2):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule SEVEN V1 \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule8(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(distance(names_list[i], names_list[j]) <= 1,
                   distance(fathers_names_list[i], fathers_names_list[j]) <= 1,
                   distance(town_list[i], town_list[j]) <= 1):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule SEVEN V1 \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule8_1(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(edit_distance(names_list[i], names_list[j]) <= 2,
                   edit_distance(fathers_names_list[i], fathers_names_list[j]) <= 2,
                   edit_distance(town_list[i], town_list[j]) <= 2):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                     convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                     convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule EIGHT AND A THIRD \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule8_2(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(edit_distance(names_list[i], names_list[j]) <= 1,
                   edit_distance(fathers_names_list[i], fathers_names_list[j]) <= 1,
                   edit_distance(town_list[i], town_list[j]) <= 1):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif rps(convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]),
                     convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]),
                     convert_to_soundex(town_list[i]) == convert_to_soundex(town_list[j])):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule EIGHT AND TWO THIRDS \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule9(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(names_list[i], names_list[j]) <= 2 or \
                    edit_distance(fathers_names_list[i], fathers_names_list[j]) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule NINE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule10(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(names_list[i], names_list[j]) <= 1 or \
                    edit_distance(fathers_names_list[i], fathers_names_list[j]) <= 1:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]) or \
                    convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule11(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if convert_to_soundex(names_list[i]) == convert_to_soundex(names_list[j]) or \
                    convert_to_soundex(fathers_names_list[i]) == convert_to_soundex(fathers_names_list[j]):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule ELEVEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule12(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(names_list[i], names_list[j]) <= 1 or \
                    edit_distance(fathers_names_list[i], fathers_names_list[j]) <= 1:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWELVE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule13(directory):
    # Damerau-Levenshtein algorithm
    case_list = case_number(directory)
    id_list = identity_number(directory)

    size = len(case_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(case_list[i], case_list[j]) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(case_list[i]) * len(case_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule THIRTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule14(directory):
    case_list = case_number(directory)
    id_list = identity_number(directory)

    size = len(case_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(case_list[i], case_list[j]) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(case_list[i]) * len(case_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1
                    print("Case Number: ", case_list[i], case_list[j])

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule FOURTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule15(directory):
    dob_list = dob(directory)
    id_list = identity_number(directory)

    size = len(dob_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(dob_list[i], dob_list[j]) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(dob_list[i]) * len(dob_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule FIFTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule16(directory):
    dob_list = dob(directory)
    id_list = identity_number(directory)

    size = len(dob_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if jaro_sim(dob_list[i], dob_list[j]) >= 0.7:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(dob_list[i]) * len(dob_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule FIFTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule17(directory):
    phone_list = phone_number(directory)
    id_list = identity_number(directory)

    size = len(phone_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(phone_list[i], phone_list[j]) <= 1:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(phone_list[i]) * len(phone_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule SEVENTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule18(directory):
    phone_list = phone_number(directory)
    id_list = identity_number(directory)

    size = len(phone_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if edit_distance(phone_list[i], phone_list[j]) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(phone_list[i]) * len(phone_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule EIGHTEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule19(directory):
    phone_list = phone_number(directory)
    id_list = identity_number(directory)

    size = len(phone_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if jaro_sim(phone_list[i], phone_list[j]) >= 0.9:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(phone_list[i]) * len(phone_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1
                    print("Numbers: ", phone_list[i], phone_list[j])

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule NINETEEN \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule20(directory):
    phone_list = phone_number(directory)
    id_list = identity_number(directory)

    size = len(phone_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if jaro_sim(phone_list[i], phone_list[j]) >= 0.8:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(phone_list[i]) * len(phone_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWENTY \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule21(directory):
    phone_list = phone_number(directory)
    id_list = identity_number(directory)

    size = len(phone_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if jaro_sim(phone_list[i], phone_list[j]) >= 0.7:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(phone_list[i]) * len(phone_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWENTY ONE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule22(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(dlev(names_list[i], names_list[j], similarity=False) <= 2,
                   dlev(fathers_names_list[i], fathers_names_list[j], similarity=False) <= 2,
                   dlev(town_list[i], town_list[j], similarity=False) <= 2):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWENTY TWO \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule23(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if dlev(names_list[i], names_list[j], similarity=False) <= 2 or \
                    dlev(fathers_names_list[i], fathers_names_list[j], similarity=False) <= 2:
                if match:
                    tp += 1
                else:
                    fp += 1
            elif len(names_list[i]) * len(names_list[j]) == 0 or \
                    len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0:
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule TWENTY THREE \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))


def rule24(directory):
    names_list = first_name(directory)
    fathers_names_list = fathers_name(directory)
    id_list = identity_number(directory)
    town_list = town_name(directory)

    size = len(names_list)
    num = count_triangle(size)

    tp, fp, fn = 0, 0, 0
    missing_info, missing_pos = 0, 0
    excluded_matches = 0

    for i in range(size):
        for j in range(i + 1, size):
            match = id_list[i][:12] == id_list[j][:12]
            if rps(dld(names_list[i], names_list[j]) <= 2,
                   dld(fathers_names_list[i], fathers_names_list[j]) <= 2,
                   dld(town_list[i], town_list[j]) <= 2):
                if match:
                    tp += 1
                else:
                    fp += 1
            elif (len(names_list[i]) * len(names_list[j]) == 0 or
                  len(fathers_names_list[i]) * len(fathers_names_list[j]) == 0 or
                  len(town_list[i]) * len(town_list[j]) == 0):
                missing_info += 1
                if match:
                    missing_pos += 1
                    tp += 1
                else:
                    fp += 1
            else:
                excluded_matches += 1
                if match:
                    print("Names : ", names_list[i], names_list[j])
                    print("F.name: ", fathers_names_list[i], fathers_names_list[j])
                    print("Towns : ", town_list[i], town_list[j])
                    fn += 1

    print("With {} records, there are {} matches to analyse".format(size, num))
    print("Using blocking rule SEVEN V2 \n{} matches are excluded "
          "\n{} matches are included because of missing data"
          "\n{} positives were found in the missing data".format(excluded_matches, missing_info, missing_pos))
    print("Blocking efficiency is {}".format(excluded_matches / num))
    print("Of the matches that are included:\n{} True Positives \n{} False Negatives "
          "\n{} False Positives".format(tp, fn, fp))
    print("Recall is {}".format(tp / (tp + fn)))