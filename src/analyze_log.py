import csv
from typing import Counter


def analyze_log(path_to_file):
    list_orders = read_to_file(path_to_file)

    item1 = food_most_ordered_by_costumer("maria", list_orders)
    item2 = quantity_ordered_by_costumer_and_food(
        "arnaldo", "hamburguer", list_orders
    )
    item3 = not_ordered_by_costumer("joao", list_orders)
    item4 = not_attended_by_costumer("joao", list_orders)

    response = (f"{item1}\n{item2}\n{item3}\n{item4}")

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(response)


def not_ordered_by_costumer(costumer_name, list_orders):
    already_ate, all_ate = set(), set()

    for order in list_orders:
        if costumer_name in order:
            already_ate.add(order[1])
        else:
            all_ate.add(order[1])

    never_ate = all_ate.symmetric_difference(already_ate)
    return never_ate


def not_attended_by_costumer(costumer_name, list_orders):
    attend, all_days = set(), set()

    for order in list_orders:
        if costumer_name in order:
            attend.add(order[2])
        else:
            all_days.add(order[2])

    does_not_attend = all_days.symmetric_difference(attend)
    return does_not_attend


def quantity_ordered_by_costumer_and_food(costumer_name, food, list_orders):
    dict_orders = []
    for order in list_orders:
        if order[0] == costumer_name and order[1] == food:
            dict_orders.append(order[1])
    return dict_orders.count(food)


def food_most_ordered_by_costumer(costumer_name, list_orders):
    most_order = []
    for order in list_orders:
        if order[0] == costumer_name:
            most_order.append(order[1])
    return Counter(most_order).most_common(1)[0][0]
    # https://docs-python-org.translate.goog/3/library/collections.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc#collections.Counter


def read_to_file(path):
    with open(path, mode="r") as file_orders:
        dict_from_csv = csv.reader(file_orders)
        list_orders = []
        for order in enumerate(dict_from_csv):
            list_orders.append(order[1])

    return list_orders


# print(analyze_log("data/orders_1.csv"))
