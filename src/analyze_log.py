import csv
from collections import Counter


def read_csv(path_to_file):
    data = []
    with open(path_to_file, mode="r") as file:
        file = csv.reader(file)
        for inf in file:
            data.append(inf)
        return data


def most_requested_by_maria(path_to_file):
    data = read_csv(path_to_file)
    maria = []
    for index in range(len(data)):
        if data[index][0] == "maria":
            maria.append(data[index][1])
    most_requested = list(Counter(maria))[0]
    return most_requested


def times_that_arnaldo_ordered_hamburger(path_to_file):
    data = read_csv(path_to_file)
    arnaldo = []
    count = int()
    for index in range(len(data)):
        if data[index][0] == "arnaldo":
            arnaldo.append(data[index][1])
    for hamburguer in arnaldo:
        if hamburguer == "hamburguer":
            count += 1
    return count


def dishes_that_joao_never_ordered(path_to_file):
    data = read_csv(path_to_file)
    dishes_joao = set()
    all_dishes = set()
    for index in range(len(data)):
        all_dishes.add(data[index][1])
        if data[index][0] == "joao":
            dishes_joao.add(data[index][1])
    not_dishes_joao = all_dishes.difference(dishes_joao)
    return not_dishes_joao


def days_that_joao_did_go_to_the_cafeteria(path_to_file):
    data = read_csv(path_to_file)
    all_days = set()
    days_of_the_joao = set()
    for index in range(len(data)):
        all_days.add(data[index][2])
        if data[index][0] == "joao":
            days_of_the_joao.add(data[index][2])
    not_days_of_the_joao = all_days.difference(days_of_the_joao)
    return not_days_of_the_joao


def analyze_log(path_to_file):
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{most_requested_by_maria(path_to_file)}\n")
        file.write(f"{times_that_arnaldo_ordered_hamburger(path_to_file)}\n")
        file.write(f"{dishes_that_joao_never_ordered(path_to_file)}\n")
        file.write(f"{days_that_joao_did_go_to_the_cafeteria(path_to_file)}\n")
