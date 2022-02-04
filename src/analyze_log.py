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
    orders = dict()
    for order in data:
        if order["name"] == customer:
            if order["food"] not in orders:
                orders[order["food"]] = 1
            else:
                orders[order["food"]] += 1
    result = max(orders, key=orders.get)
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
def not_ordered(data):
    ordered_food = set()
    for order in data:
        if order["name"] == "joao":
            ordered_food.add(order["food"])
    all_orders = set([i["food"] for i in data])
    not_ordered = all_orders.difference(ordered_food)
    # Difference retorna um set novo com os itens
    # que somente tem no primeiro set.
    # Src =
    # https://www.w3schools.com/python/ref_set_difference.asp#:~:text=The%20difference()%20method%20returns,and%20not%20in%20both%20sets.
    return not_ordered


# Quais dias 'joao' nunca foi na lanchonete?
def not_visited(data):
    visited_days = set([day["day"] for day in data])
    joao_log = set()
    for date in data:
        if date["name"] == "joao":
            joao_log.add(date["day"])
    return visited_days.difference(joao_log)


def txt(text, txt_file):
    with open(txt_file, "w") as file:
        file.write(text)


def analyze_log(path_to_file):
    # raise NotImplementedError
    data = read_csv(path_to_file)
    maria_fav = maria_fav_food(data, "maria")
    arnaldo_orders = arnaldo_burguer(data)
    joao_not_ordered = not_ordered(data)
    joao_not_visited = not_visited(data)

    result = (
        f"{maria_fav}\n"
        + f"{arnaldo_orders}\n"
        + f"{joao_not_ordered}\n"
        + f"{joao_not_visited}\n"
    )
    txt(result, "data/mkt_campaign.txt")
