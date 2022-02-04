import csv
from collections import Counter


def get_csv(path_file):

    with open(path_file, mode="r") as file:
        reader = csv.reader(file)
        result = list(reader)
        return result


def most_ordered(path_file):
    csv_list = get_csv(path_file)
    maria_list = []

    for item in range(len(csv_list)):
        if csv_list[item][0] == "maria":
            maria_list.append(csv_list[item][1])

    counter = Counter(maria_list)

    return list(counter)[0]


def most_ordered_hamburguer(path_file):
    list = get_csv(path_file)
    total = 0

    for item in range(len(list)):
        if (list[item][0] == "arnaldo" and list[item][1] == "hamburguer"):
            total += 1

    return total


def never_asked_dishes(path_file):
    csv_list = get_csv(path_file)
    all_dishes = set()
    orders = set()

    for item in range(len(csv_list)):
        all_dishes.add(csv_list[item][1])
        if csv_list[item][0] == "joao":
            orders.add(csv_list[item][1])

    return all_dishes.difference(orders)


def days_never_went(path_file):
    csv_list = get_csv(path_file)
    all_days = set()
    joao_days = set()

    for item in range(len(csv_list)):
        all_days.add(csv_list[item][2])
        if csv_list[item][0] == "joao":
            joao_days.add(csv_list[item][2])

    return all_days.difference(joao_days)


def analyze_log(path_to_file):

    with open('./data/mkt_campaign.txt', mode="w") as result_list:
        result_list.write(f"{most_ordered(path_to_file)}\n")
        result_list.write(f"{most_ordered_hamburguer(path_to_file)}\n")
        result_list.write(f"{never_asked_dishes(path_to_file)}\n")
        result_list.write(f"{days_never_went(path_to_file)}\n")
