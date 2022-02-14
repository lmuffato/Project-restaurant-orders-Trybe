import csv


def read_path(path):
    with open(path) as file:
        csv_file = csv.reader(file)
        data = [row for row in csv_file]

    return data


def get_by_meals(path):
    with open(path) as file:
        csv_file = csv.reader(file)
        data = [row[1] for row in csv_file]

    return list(set(data))


def get_days_by_person(path, person):
    days_person_ordered = []
    with open(path) as file:
        csv_file = csv.reader(file)
        all_days = [row[2] for row in csv_file]

    data_by_path = read_path(path)
    for row in data_by_path:
        if row[0] == person:
            days_person_ordered.append(row[2])

    return set(all_days) - set(days_person_ordered)


def get_orders_by_person(path, person):
    orders_number = {}

    with open(path) as file:
        csv_file = csv.reader(file)
        data_person = [row for row in csv_file if row[0] == person]
        for row in data_person:
            if row[1] in orders_number:
                orders_number[row[1]] += 1
            else:
                orders_number[row[1]] = 1

    return orders_number


def analyze_log(path_to_file):
    data_by_meals = get_by_meals(path_to_file)

    ordered_by_maria = get_orders_by_person(path_to_file, 'maria')
    most_ordered_by_maria = max(ordered_by_maria, key=ordered_by_maria.get)

    ordered_by_arnaldo = get_orders_by_person(path_to_file, 'arnaldo')
    biggest_ordered_by_burger = ordered_by_arnaldo['hamburguer']

    ordered_by_joao = get_orders_by_person(path_to_file, 'joao')
    less_ordered_by_joao = set([
        orders for orders in data_by_meals
        if orders not in ordered_by_joao.keys()
    ])

    did_not_go_by_joao = get_days_by_person(path_to_file, 'joao')
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(most_ordered_by_maria) + '\n')
        file.write(str(biggest_ordered_by_burger) + '\n')
        file.write(str(less_ordered_by_joao) + '\n')
        file.write(str(did_not_go_by_joao) + '\n')
