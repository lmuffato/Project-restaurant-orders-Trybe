import statistics
from collections import Counter
import csv


def read_path(path):
    if path.endswith(".csv"):
        with open(path, 'r') as file:
            return list(csv.reader(file, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def most_requested_food_by_maria(data):
    foods = []
    for list in data:
        name = list[0]
        if name == 'maria':
            foods.append(list[1])
    return statistics.mode(foods)


def many_times_arnaldo_ordered_for_hamburguer(data, food):
    foods = []
    for list in data:
        name = list[0]
        if name == 'arnaldo':
            if list[1] == food:
                foods.append(list[1])
    return Counter(foods).most_common(1)[0][1]


def joao_never_ordered_food(data):
    menu = set()
    joao_ordered = set()
    for list in data:
        name = list[0]
        food = list[1]
        menu.add(food)
        if name == 'joao':
            joao_ordered.add(food)
    return menu.difference(joao_ordered)


def joao_never_went_to_lanchonete(data):
    days_in_week = set()
    days_joao = set()
    for list in data:
        days = list[2]
        name = list[0]
        days_in_week.add(days)
        if name == 'joao':
            days_joao.add(days)
    return days_in_week.difference(days_joao)


def analyze_log(path_to_file):
    data = read_path(path_to_file)
    food_maria = most_requested_food_by_maria(data)
    many_times_arnaldo = many_times_arnaldo_ordered_for_hamburguer(
        data, 'hamburguer'
    )
    joao_never_ordered = joao_never_ordered_food(data)
    joao_never_went = joao_never_went_to_lanchonete(data)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{food_maria}\n'
            f'{many_times_arnaldo}\n'
            f'{joao_never_ordered}\n'
            f'{joao_never_went}'
        )
