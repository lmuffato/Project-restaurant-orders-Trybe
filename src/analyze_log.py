# começando
import csv


def read_csv(path):
    with open(path) as file:
        return list(csv.reader(file, delimiter=","))


def pedidos(name, data):
    result = list()
    for client in data:
        if client[0] == name:
            result.append(client[1])
    return max(set(result), key=result.count)


def hambuguers_pedidos(name, data):
    count = 0
    for client in data:
        if client[0] == name and client[1] == "hamburguer":
            count += 1
    return count


def nunca_pedidos(name, data):
    client_order = []
    recipes = []
    for row in data:
        recipes.append(row[1])
        if row[0] == name:
            client_order.append(row[1])
    return set(recipes).symmetric_difference(set(client_order))


def dias(name, data):
    client_order = []
    days = []
    for row in data:
        days.append(row[2])
        if row[0] == name:
            client_order.append(row[2])
    return set(days).symmetric_difference(set(client_order))


def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    maria_pedidos = pedidos("maria", data)
    arnaldo_hamburguer = hambuguers_pedidos("arnaldo", data)
    joao_nunca = nunca_pedidos("joao", data)
    dias_nunca = dias("joao", data)

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(
            [
                f"{maria_pedidos}\n",
                f"{arnaldo_hamburguer}\n",
                f"{joao_nunca}\n",
                f"{dias_nunca}\n",
            ]
        )
