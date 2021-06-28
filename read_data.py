import csv


def identity_number(file_directory):  # returns list of ID numbers

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[0])

    return names_list


def first_name(file_directory):  # returns list of names

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[2].upper())

    return names_list


def fathers_name(file_directory):  # returns list of names

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[3].upper())

    return names_list


def town_name(file_directory):  # returns list of names

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[10].upper())

    return names_list


def case_number(file_directory):  # returns list of names

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[1].upper())

    return names_list


def phone_number(file_directory):

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[11].upper())

    return names_list


def dob(file_directory):

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append(row[8].upper())

    return names_list


def first_and_fathers_tuple(file_directory):

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append((row[2].upper(), row[3].upper()))

    return names_list


def full(file_directory):

    # first name, father's name, case report number, DOB, phone number

    names_list = []

    with open(file_directory) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            names_list.append((row[1], row[11], row[2], row[3], row[8]))

    return names_list
