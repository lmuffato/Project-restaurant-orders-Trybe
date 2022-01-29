# # Glossário
# endswith:
# https://www.programiz.com/python-programming/methods/string/endswith
# O endswith() retorna True se uma string termina com o sufixo especificado.
# Se não, ele retorna False
# FileNotFoundError:
# https://docs.python.org/pt-br/3/library/exceptions.html
# Levantada quando um arquivo ou diretório é solicitado, mas não existe.

import csv

# Recupra os dados do arquivo csv


def file_reader(path):

    if path.endswith("csv"):
        with open(path) as data:
            return list(csv.reader(data, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


# Retorna o prato mais pedido de acordo com o cliente
def most_request_dish(data, client):
    dishes = []

    for requests in data:
        if requests[0] == client:
            dishes.append(requests[1])
    return max(set(dishes), key=dishes.count)


# Retorna a quantidade de vezes que um cliente pediu um prato
def orders_per_dish(data, client, dish):
    dishes = []
    for requests in data:
        if requests[0] == client and requests[1] == dish:
            dishes.append(requests[1])
    return len(dishes)


# Retorna o prato que um cliente nunca pediu
def dishes_never_asked(data, client):

    dishes = [requests[1] for requests in data]

    for requests in data:
        if requests[0] == client:
            for dish in dishes:
                if dish == requests[1]:
                    dishes.remove(dish)

    return set(dishes)


# Retorna o dia quue o cliente não foi a lanchonete
def missed_which_day(data, client):
    days_of_week = [requests[2] for requests in data]

    for requests in data:
        if requests[0] == client:
            for day in days_of_week:
                if day == requests[2]:
                    days_of_week.remove(day)

    return set(days_of_week)


def analyze_log(path_to_file):
    DATA = file_reader(path_to_file)
    most_request_dish_by = most_request_dish(DATA, "maria")
    number_of_orders = orders_per_dish(DATA, "arnaldo", "hamburguer")
    dish_never_ordered_by = dishes_never_asked(DATA, "joao")
    never_been_in_the_day = missed_which_day(DATA, "joao")

    result = [
        f"{most_request_dish_by}\n",
        f"{number_of_orders}\n",
        f"{dish_never_ordered_by}\n",
        f"{never_been_in_the_day}\n",
    ]
    with open("data/mkt_campaign.txt", "w") as data:
        data.writelines(result)
