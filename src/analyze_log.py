import csv
from collections import Counter


def reader(path):
    with open(path) as file:
        return list(csv.reader(file))

def favorite_recipes(name, orders):
    all_orders = []
    for order in orders:
        if order[0] == name:
            all_orders.append(order[1])
    counter = Counter(all_orders).most_common(1)[0][0]
    return counter

def counting_ordered(name, meal, orders):
    counter = 0
    for order in orders:
        if order[0] == name and order[1] == meal:
            counter += 1
    return counter


def meals_not_ordered(name, orders):
    all_meals = set()
    one_meal = set()
    for order in orders:
        all_meals.add(order[1])
    for order in orders:
        if order[0] == name:
            one_meal.add(order[1])
    return all_meals.difference(one_meal)


def days_without_order(name, days):
    all_days = set()
    client_days = set()
    for day in days:
        all_days.add(day[2])
    for client in days:
        if client[0] == name:
            client_days.add(client[2])
    return all_days.difference(client_days)


def analyze_log(path_to_file):
    result = ''
    data = reader(path_to_file)
    favorite_meals = favorite_recipes('maria', data)
    counter = counting_ordered('arnaldo', 'hamburguer', data)
    not_ordered = meals_not_ordered('joao', data)
    days_no_order = days_without_order('joao', data)
    result = f'{favorite_meals}\n{counter}\n{not_ordered}\n{days_no_order}'
    file = open("data/mkt_campaign.txt", "w")
    file.write(result)
    file.close()
