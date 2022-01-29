import csv


def csv_import(path):
    data = []

    with open(path, mode="r") as file:
        list = csv.reader(file)

        for name, food, week in list:
            data.append({"name": name, "food": food, "week": week})
    return data


def most_requested_by_Maria(orders):
    most_frequent_eat = orders[0]["food"]
    frequency = {}

    for order in orders:
        if order["name"] == "maria":
            if order["food"] not in frequency:
                frequency[order["food"]] = 1
            else:
                frequency[order["food"]] += 1
            if frequency[order["food"]] > frequency[most_frequent_eat]:
                most_frequent_eat = order["food"]

    return most_frequent_eat


def amount_hamburguer_order_by_Arnaldo(orders):
    amount = 0
    for order in orders:
        if order["name"] == "arnaldo" and order["food"] == "hamburguer":
            amount += 1
    return amount


def dishs_never_order_by_Joao(orders):
    list = []
    list_not_order_food = []
    for order in orders:
        if order["name"] == "joao" and order["food"] not in list:
            list.append(order["food"])
            # orders_checked[order['food']] = True

    for order in orders:
        if (
            order["food"] not in list
            and order["food"] not in list_not_order_food
        ):
            list_not_order_food.append(order["food"])
    return list_not_order_food


def days_Joao_never_went(orders):
    list = []
    list_day_never_went = []
    for order in orders:
        if order["name"] == "joao" and order["week"] not in list:
            list.append(order["week"])
            # orders_checked[order['food']] = True

    for order in orders:
        if (
            order["week"] not in list
            and order["week"] not in list_day_never_went
        ):
            list_day_never_went.append(order["week"])
    return list_day_never_went


def analyze_log(path_to_file):
    data = csv_import(path_to_file)
    most_requested_by_Maria(data)
    amount_hamburguer_order_by_Arnaldo(data)
    dishs_never_order_by_Joao(data)
    days_Joao_never_went(data)
    raise NotImplementedError(data)
