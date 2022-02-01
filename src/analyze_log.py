from csv import DictReader
from collections import Counter


# Função auxiliar
def reader(path_to_file):
    with open(path_to_file, mode="r") as orders:
        data = []
        data_read = DictReader(orders)
        for order in data_read:
            data.append(order)


# mais pedidos de maria
def maria_most_ordered(path_to_file):
    data = reader(path_to_file)
    maria_orders = []
    for index in range(len(data)):
        if data[index][0] == "maria":
            maria_orders.append(data[index][1])
    most_ordered = list(Counter(maria_orders)[0])
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


def analyze_log(path_to_file):
    with open("./data/mkt_campaing.txt", mode="w") as file:
        file.write(f"{maria_most_ordered(path_to_file)}\n")
        file.write(f"{arnaldo_burguers(path_to_file)}\n")
        file.write(f"{dishes_joao_never_ordered(path_to_file)}\n")
    raise NotImplementedError
