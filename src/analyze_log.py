import csv


def read_csv(path_to_file):
    data = []
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for name, food, day in reader:
            data.append({
                "name": name,
                "food": food,
                "day": day
            })
    return data


# Qual o prato mais pedido por 'maria'?
def maria_fav_food(data, customer):
    dicionario = dict()
    for i in data:
        if i["name"] == customer:
            if i["food"] not in dicionario:
                dicionario[i["food"]] = 1
            else:
                dicionario[i["food"]] += 1
    result = max(dicionario, key=dicionario.get)
    return result


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
def arnaldo_burguer(data):
    orders = 0
    for order in data:
        if order["name"] == "arnaldo":
            if order["food"] == "hamburguer":
                orders += 1
    return orders


# Quais pratos 'joao' nunca pediu?
def not_asked(data):
    orders = set()
    for order in data:
        if order["name"] == "joao":
            orders.add(order["food"])


def txt(text, txt_file):
    with open(txt, "w") as file:
        file.write(text)


def analyze_log(path_to_file):
    # raise NotImplementedError
    data = read_csv(path_to_file)
    maria_fav = maria_fav_food(data, "maria")
    arnaldo_orders = arnaldo_burguer(data)

    result = (
        f"{maria_fav}\n"
        + f"{arnaldo_orders}"
    )
    txt(result, "data/mkt_campaign.txt")
