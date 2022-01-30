import csv
from collections import Counter


def how_many_name_dice(name, dice, data):
    count = 0
    for order in data:
        if order[0] == name and order[1] == dice:
            count += 1
    return count


def more_dice_name(name, data):
    client = []
    for item in data:
        if item[0] == name:
            client.append(item[1])
    result = Counter(client).most_common(1)[0][0]
    return result


def pratos_nunca_pedidos(name, all_dices, data):
    pratos_pedidos = set()
    for item in data:
        if item[0] == name:
            pratos_pedidos.add(item[1])
    return all_dices.difference(pratos_pedidos)


def dias_sem_atendimento(name, expediente, data):
    dias_pedidos = set()
    for item in data:
        if item[0] == name:
            dias_pedidos.add(item[2])
    return expediente.difference(dias_pedidos)


def analyze_log(path_to_file):

    with open(path_to_file) as csvfile:
        data = []
        menu_options = set()
        dias_de_expediente = set()
        spamreader = csv.reader(csvfile)

        for row in spamreader:
            menu_options.add(row[1])
            dias_de_expediente.add(row[2])
            data.append(row)

        item1 = more_dice_name("maria", data)
        item2 = how_many_name_dice("arnaldo", "hamburguer", data)
        item3 = pratos_nunca_pedidos("joao", menu_options, data)
        item4 = dias_sem_atendimento("joao", dias_de_expediente, data)
        result = f"{item1}\n"
        result += f"{item2}\n"
        result += f"{item3}\n"
        result += f"{item4}\n"

        with open("data/mkt_campaign.txt", "w") as f:
            f.write(result)
