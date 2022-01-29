import csv


def csv_import(path):
    data = []

    with open(path, mode="r") as file:
        list = csv.reader(file)

        for name, food, week in list:
            data.append({"name": name, "food": food, "week": week})
    return data


def most_requested_by_Maria(orders):
    most_frequent_eat = orders[0]['food']
    frequency = {}

    for order in orders:
        if order['name'] == 'maria':
            if order['food'] not in frequency:
                frequency[order['food']] = 1
            else:
                frequency[order['food']] += 1
            if frequency[order['food']] > frequency[most_frequent_eat]:
                most_frequent_eat = order['food']

    return most_frequent_eat


def amount_hamburguer_order_by_Arnaldo(orders):
    amount = 0
    for order in orders:
        if order['name'] == 'arnaldo' and order['food'] == 'hamburguer':
            amount += 1
    return amount


def analyze_log(path_to_file):
    data = csv_import(path_to_file)
    most_requested_by_Maria(data)
    amount_hamburguer_order_by_Arnaldo(data)
    raise NotImplementedError(data)
