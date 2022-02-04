import csv


def get_favorite_order(file):
    data = csv.reader(file)
    maria_orders = []
    for row in data:
        if row[0] == "maria":
            maria_orders.append(row[1])
    return max(set(maria_orders), key=maria_orders.count)


def get_order_count(file):
    data = csv.reader(file)
    count = 0
    for row in data:
        if row[0] == "arnaldo" and row[1] == "hamburguer":
            count += 1
    return count


def never_ask(file):
    data = csv.reader(file)
    joao_orders = []
    recipes = []
    for row in data:
        recipes.append(row[1])
        if row[0] == "joao":
            joao_orders.append(row[1])
    return set(recipes).symmetric_difference(set(joao_orders))


def never_went(file):
    data = csv.reader(file)
    joao_orders = []
    days = []
    for row in data:
        days.append(row[2])
        if row[0] == "joao":
            joao_orders.append(row[2])
    return set(days).symmetric_difference(set(joao_orders))


def analyze_log(path_to_file):
    maria_eats = get_favorite_order(open(path_to_file))
    arnaldo_ask = get_order_count(open(path_to_file))
    joao_never_ask = never_ask(open(path_to_file))
    joao_never_went = never_went(open(path_to_file))
    new_file = open("data/mkt_campaign.txt", "w")
    new_file.write(maria_eats)
    new_file.write(f"\n{arnaldo_ask}")
    new_file.write(f"\n{joao_never_ask}")
    new_file.write(f"\n{joao_never_went}")
    new_file.close()


analyze_log("data/orders_1.csv")
