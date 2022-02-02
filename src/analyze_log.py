import csv


def maria_fav_food(orders):
    foods = {}
    biggest_quantity = 0
    fav_food = ''
    for order in orders:

        if order[0] not in foods:
            foods[order[0]] = 1
        else:
            foods[order[0]] += 1
        if foods[order[0]] > biggest_quantity:
            biggest_quantity = foods[order[0]]
            fav_food = order[0]
    return fav_food


def analyze_log(path_to_file):
    orders = {}
    with open(path_to_file) as file:
        # Fonte: https://docs.python.org/3/library/csv.html
        reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in reader:
            if row[0] not in orders:
                orders[row[0]] = [[row[1], row[2]]]
            else:
                orders[row[0]].append([row[1], row[2]])

    print(maria_fav_food(orders['maria']))
