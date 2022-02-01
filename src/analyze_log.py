import csv
from collections import Counter

# Referencia: https://app.betrybe.com/course/computer-science
# /introducao-a-python/aprendendo-python/9c4e1d64-303d-492d-82a4-998b2c0218b9/
# conteudos/217980af-0946-4b04-9cc4-5846af26ec27/tipos-de-dados-embutidos/bea4b2ef-aece-43fe-9d9d-fa7d8c183088?use_case=side_bar
# Função auxiliar


def reader(path_to_file):
    with open(path_to_file, mode="r") as orders:
        data_read = csv.reader(orders)
        return list(data_read)


# mais pedidos de maria
def maria_most_ordered(path_to_file):
    data = reader(path_to_file)
    maria_orders = []
    for index in range(len(data)):
        if data[index][0] == "maria":
            maria_orders.append(data[index][1])
    most_ordered = list(Counter(maria_orders))[0]
    return most_ordered


# Quantas vezes Arnaldo pediu Hamburguer


def arnaldo_burguers(path_to_file):
    data = reader(path_to_file)
    total_hamburguers = int()
    for index in range(len(data)):
        if data[index][0] == "arnaldo" and data[index][1] == "hamburguer":
            total_hamburguers += 1
    return total_hamburguers


def dishes_joao_never_ordered(path_to_file):
    data = reader(path_to_file)
    all_dishes = set()
    joao_dishes = set()
    for index in range(len(data)):
        all_dishes.add(data[index][1])
        if data[index][0] == "joao":
            joao_dishes.add(data[index][1])
    not_ordered_by_joao = all_dishes.difference(joao_dishes)
    return not_ordered_by_joao


def days_joao_dont_go_to_restaurant(path_to_file):
    data = reader(path_to_file)
    every_day = set()
    joao_days = set()
    for index in range(len(data)):
        every_day.add(data[index][2])
        if data[index][0] == 'joao':
            joao_days.add(data[index][2])
    days_joao_dont_go_to_restaurant = every_day.difference(joao_days)
    return days_joao_dont_go_to_restaurant


def analyze_log(path_to_file):
    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(f"{maria_most_ordered(path_to_file)}\n")
        file.write(f"{arnaldo_burguers(path_to_file)}\n")
        file.write(f"{dishes_joao_never_ordered(path_to_file)}\n")
        file.write(f"{days_joao_dont_go_to_restaurant(path_to_file)}\n")
