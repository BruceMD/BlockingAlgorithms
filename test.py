from read_data import first_name, identity_number, first_and_fathers_tuple
from levenshtein_distance_algorithm import edit_distance
from soundex_convert_algorithm import convert_to_soundex
from jaro_similarity_algorithm import jaro_sim
from jaro_winkler_similarity_algorithm import jw_similarity
from double_metaphone_algorithm import mod_dmetaphone, compare_dmetaphone


def jw_similarity_first_names_only(file_directory):
    names = first_name(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            total_matches += 1
            if jw_similarity(names[i], names[j]) >= 0.8:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i]) * len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def jw_similarity_first_fathers_names(file_directory):
    names = first_and_fathers_tuple(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            total_matches += 1
            if jw_similarity(names[i][0], names[j][0]) >= 0.8 or jw_similarity(names[i][1], names[j][1]) >= 0.8:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i][0]) * len(names[j][0]) == 0 and len(names[i][1]) * len(names[j][1]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def dmetaphone_test_first_name_only(file_directory):
    names = first_name(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        ref_name = mod_dmetaphone(names[i])
        for j in range(i + 1, len(names)):
            total_matches += 1
            compare_name = mod_dmetaphone(names[j])
            if compare_dmetaphone(ref_name, compare_name):
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i]) * len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def dmetaphone_test_first_fathers_name(file_directory):
    names = first_and_fathers_tuple(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        ref_name = mod_dmetaphone(names[i][0])
        ref_surname = mod_dmetaphone(names[i][1])
        for j in range(i + 1, len(names)):
            total_matches += 1
            compare_name = mod_dmetaphone(names[j][0])
            compare_surname = mod_dmetaphone(names[j][1])
            if compare_dmetaphone(ref_name, compare_name) or compare_dmetaphone(ref_surname, compare_surname):
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i]) * len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
#                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def jaro_first_name_only(file_directory):
    names = first_name(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            total_matches += 1
            if jaro_sim(names[i], names[j]) >= 0.85:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i]) * len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
    #                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def jaro_first_fathers_name(file_directory):

    # going to look at ED for name, father's name
    # if any return as a suitable match, then we will include it

    names = first_and_fathers_tuple(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            total_matches += 1
            if jaro_sim(names[i][0], names[j][0]) >= 0.85 or jaro_sim(names[i][1], names[j][1]) >= 0.85:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i][0])*len(names[j][0]) == 0 and len(names[i][1])*len(names[j][1]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
#                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def soundex_first_name_only(file_directory):
    names = first_name(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        ref_name = convert_to_soundex(names[i])
        for j in range(i + 1, len(names)):
            total_matches += 1
            if ref_name == convert_to_soundex(names[j]):
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i]) * len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
#                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def soundex_first_fathers_name(file_directory):
    names = first_and_fathers_tuple(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        ref_name = convert_to_soundex(names[i][0])
        ref_father_name = convert_to_soundex(names[i][1])
        for j in range(i + 1, len(names)):
            total_matches += 1

            if ref_name == convert_to_soundex(names[j][0]) or ref_father_name == convert_to_soundex(names[j][1]):
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i][0]) * len(names[j][0]) == 0 and len(names[i][1]) * len(names[j][1]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
#                    print(names[i], names[j])

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))


def levenshtein_first_fathers_name(file_directory):

    # going to look at ED for name, father's name
    # if any return as a suitable match, then we will include it

    names = first_and_fathers_tuple(file_directory)
    id_nums = identity_number(file_directory)

    dup = 0
    double_dup = 0

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        if "bbb" in id_nums[i]:
            dup += 1
            if "bbb-1" in id_nums[i]:
                double_dup += 1
        for j in range(i+1, len(names)):
            total_matches += 1
            if edit_distance(names[i][0], names[j][0]) < 3 or edit_distance(names[i][1], names[j][1]) < 3:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i][0])*len(names[j][0]) == 0 and len(names[i][1])*len(names[j][1]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
#                    print("Names:          ", names[i][0], names[j][0])
#                    print("Father's names: ", names[i][1], names[j][1])
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1

    print("Out of {} total matches:\n{} are TP \n{} are FN \n{} are FP".format(total_matches, tp, fn, fp))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))
    print("Duplications total: {}\nDouble duplications: {}".format(dup, double_dup))


def test_levenshtein_first_name_only(file_directory):

    names = first_name(file_directory)
    id_nums = identity_number(file_directory)

    total_matches = 0
    tp, fp, fn = 0, 0, 0
    missing_field, missed_positives = 0, 0

    for i in range(len(names)):
        for j in range(i+1, len(names)):
            total_matches += 1
            if edit_distance(names[i], names[j]) < 3:
                if id_nums[i][:12] == id_nums[j][:12]:
                    tp += 1
                else:
                    fp += 1
            elif len(names[i])*len(names[j]) == 0:
                missing_field += 1
                if id_nums[i][:12] == id_nums[j][:12]:
                    missed_positives += 1
            else:
                if id_nums[i][:12] == id_nums[j][:12]:
                    fn += 1
#                    print(names[i], names[j])
#                    print(convert_to_soundex(names[i]), convert_to_soundex(names[j]))

    print("Out of {} total matches:\n{} are TP \n{} are FP \n{} are FN".format(total_matches, tp, fp, fn))
    print("Out of {} missing names instances, {} were missed positives".format(missing_field, missed_positives))
