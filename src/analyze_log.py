import csv


def csv_import(path):
    data = []

    with open(path, mode="r") as file:
        list = csv.reader(file)

        for name, food, week in list:
            data.append({"name": name, "food": food, "week": week})
    return data


def most_requested_by_Maria(orders):
    most_frequent_eat = orders[0]['comida']
    frequency = {}

    for order in orders:
        if order['nome'] == 'maria':
            if order['comida'] not in frequency:
                frequency[order['comida']] = 1
            else:
                frequency[order['comida']] += 1
            if frequency[order['comida']] > frequency[most_frequent_eat]:
                most_frequent_eat = order['comida']

    return most_frequent_eat


def analyze_log(path_to_file):
    data = csv_import(path_to_file)
    most_requested_by_Maria(data)
    raise NotImplementedError(data)
