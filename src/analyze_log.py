import csv


def dish_favorite_maria(logs):
    logs_maria = [log for log in logs if log[0] == "maria"]

    favorite_dish_maria = logs[0][1]
    dishs_maria = {}

    for log in logs_maria:
        if log[1] in dishs_maria:
            dishs_maria[log[1]] += 1
        else:
            dishs_maria[log[1]] = 0

        if dishs_maria[log[1]] > dishs_maria[favorite_dish_maria]:
            favorite_dish_maria = log[1]

    return favorite_dish_maria


def hamburguer_arnaldo(logs):
    quantity_hamburguer_arnaldo = 0

    for log in logs:
        if log[0] == "arnaldo" and log[1] == "hamburguer":
            quantity_hamburguer_arnaldo += 1

    return quantity_hamburguer_arnaldo


def food_joao_not_like(logs):
    all_foods = set()
    food_joao = set()

    for log in logs:
        all_foods.add(log[1])
        if log[0] == "joao":
            food_joao.add(log[1])

    return all_foods - food_joao


def days_joao_not_eat(logs):
    all_days = set()
    days_joao = set()

    for log in logs:
        all_days.add(log[2])
        if log[0] == "joao":
            days_joao.add(log[2])

    return all_days - days_joao


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        reader_file = csv.reader(file)
        logs = [i for i in reader_file]
    favorite_dish_maria = dish_favorite_maria(logs)
    quantity_hamburguer_arnaldo = hamburguer_arnaldo(logs)
    joao_not_like = food_joao_not_like(logs)
    days_joao_not_go_eat = days_joao_not_eat(logs)

    file = open("data/mkt_campaign.txt", mode="w")
    file.write(f"{favorite_dish_maria}\n")
    file.write(f"{quantity_hamburguer_arnaldo}\n")
    file.write(f"{joao_not_like}\n")
    file.write(f"{days_joao_not_go_eat}")
