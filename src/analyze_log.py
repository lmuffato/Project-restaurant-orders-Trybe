import statistics
from collections import Counter
import csv


def read_path(path):
    if path.endswith(".csv"):
        with open(path, 'r') as file:
            return list(csv.reader(file, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def most_requested_food_by_customer(data, customer):
    foods = []
    for list in data:
        name = list[0]
        if name == customer:
            foods.append(list[1])
    return statistics.mode(foods)


def many_times_arnaldo_ordered_for_hamburguer(data, customer):
    foods = []
    for list in data:
        name = list[0]
        food = 'hamburguer'
        if name == customer:
            if list[1] == food:
                foods.append(list[1])
    return Counter(foods).most_common(1)[0][1]


def customer_never_ordered_food(data, customer):
    menu = set()
    joao_ordered = set()
    for list in data:
        name = list[0]
        food = list[1]
        menu.add(food)
        if name == customer:
            joao_ordered.add(food)
    return menu.difference(joao_ordered)


def customer_never_went_to_lanchonete(data, customer):
    days_in_week = set()
    days_joao = set()
    for list in data:
        days = list[2]
        name = list[0]
        days_in_week.add(days)
        if name == customer:
            days_joao.add(days)
    return days_in_week.difference(days_joao)


def busiest_day(data):
    days = []
    for list in data:
        days.append(list[2])
    return statistics.mode(days)


def least_busy_day(data):
    """"referencia Felipe Flores"""
    days_with_costumer_count = {}
    for list in data:
        day = list[2]
        if day not in days_with_costumer_count:
            days_with_costumer_count[day] = 1
        else:
            days_with_costumer_count[day] += 1
    itemMinValue = min(days_with_costumer_count.items(), key=lambda x: x[1])
    return itemMinValue[0]


def analyze_log(path_to_file):
    data = read_path(path_to_file)
    food_maria = most_requested_food_by_customer(data, 'maria')
    many_times_arnaldo = many_times_arnaldo_ordered_for_hamburguer(
        data, 'arnaldo'
    )
    joao_never_ordered = customer_never_ordered_food(data, 'joao')
    joao_never_went = customer_never_went_to_lanchonete(data, 'joao')
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{food_maria}\n'
            f'{many_times_arnaldo}\n'
            f'{joao_never_ordered}\n'
            f'{joao_never_went}'
        )
