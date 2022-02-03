import csv


def all_days(path_to_file):
    days = set()
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[2] not in days:
                days.add(row[2])
    return days


def all_foods(path_to_file):
    foods = set()
    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[1] not in foods:
                foods.add(row[1])
    return foods


def csv_reader(path_to_file):
    orders = {}
    with open(path_to_file) as file:
        # Fonte: https://docs.python.org/3/library/csv.html
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in orders:
                orders[row[0]] = [[row[1], row[2]]]
            else:
                orders[row[0]].append([row[1], row[2]])
    return orders
