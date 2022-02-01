import csv
from collections import Counter


# csv_to_list
# https://qastack.com.br/programming/24662571/python-import-csv-to-list
def csv_to_list(path_to_file):
    with open(path_to_file, mode="r") as f:
        reader = csv.reader(f)
        data = list(reader)
        return data


def maria_orders(path_to_file):
    data = csv_to_list(path_to_file)
    maria_ham = []
    for i in range(len(data)):
        if data[i][0] == "maria":  # pega primeiro item da lista
            maria_ham.append(
                data[i][1]
            )  # guarda segundo item da lista que é o alimento
    counter = Counter(maria_ham)
    return list(counter)[0]


def arnaldo_order_ham(path_to_file):
    data = csv_to_list(path_to_file)
    hams = 0
    for i in range(len(data)):
        if (
            data[i][0] == "arnaldo" and data[i][1] == "hamburguer"
        ):  # confere pessoa e alimento e soma pedidos
            hams += 1
    return int(hams)


def joao_didnt_ask(path_to_file):
    data = csv_to_list(path_to_file)
    dishes = set()  # usa o set para não repetir
    joao_dishes = set()
    for i in range(len(data)):
        dishes.add(data[i][1])  # pega todos os pratos
        if data[i][0] == "joao":
            joao_dishes.add(data[i][1])  # guarda os pratos do joão
    return dishes.difference(joao_dishes)
    # retorna diferença dos pratos que joão nao pediu


def joao_didnt_go(path_to_file):
    data = csv_to_list(path_to_file)
    all_days = set()
    joao_days = set()
    for i in range(len(data)):
        all_days.add(data[i][2])  # guarda o todos os dias
        if data[i][0] == "joao":  # dias do joão
            joao_days.add(data[i][2])  # todos os dias que joão
    return all_days.difference(joao_days)


def analyze_log(path_to_file):
    with open("./data/mkt_campaign.txt", mode="w") as arquivo:
        arquivo.write(f"{maria_orders(path_to_file)}\n")
        arquivo.write(f"{arnaldo_order_ham(path_to_file)}\n")
        arquivo.write(f"{joao_didnt_ask(path_to_file)}\n")
        arquivo.write(f"{joao_didnt_go(path_to_file)}\n")
