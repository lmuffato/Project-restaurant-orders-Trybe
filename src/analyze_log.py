import csv
from typing import Counter


def analyze_log(path_to_file):
    list_orders = read_to_file(path_to_file)

    maria_favorite_food = food_most_ordered_by_customer("maria", list_orders)
    arnaldo_hamburger_orders = quantity_ordered_by_customer_and_food(
        "arnaldo", "hamburguer", list_orders
    )
    joao_not_attended = not_attended_and_not_ordered_by_customer(
        "joao", list_orders
    )
    response = (
        f"{maria_favorite_food}{arnaldo_hamburger_orders}{joao_not_attended}"
    )

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.write(response)


def not_attended_and_not_ordered_by_customer(customer_name, list_orders):
    already_ate = set()
    all_ate = set()

    attend = set()
    all_days = set()

    for order in list_orders:
        if customer_name in order:
            already_ate.add(order[1])
            attend.add(order[2])
        else:
            all_ate.add(order[1])
            all_days.add(order[2])

    never_ate = all_ate.symmetric_difference(already_ate)
    does_not_attend = all_days.symmetric_difference(attend)

    return f"{never_ate}\n{does_not_attend}"


def quantity_ordered_by_customer_and_food(customer_name, food, list_orders):
    dict_orders = []
    for order in list_orders:
        if order[0] == customer_name and order[1] == food:
            dict_orders.append(order[1])
    return f"{dict_orders.count(food)}\n"


def food_most_ordered_by_customer(customer_name, list_orders):
    most_order = []
    for order in list_orders:
        if order[0] == customer_name:
            most_order.append(order[1])
    return f"{Counter(most_order).most_common(1)[0][0]}\n"
    # https://docs-python-org.translate.goog/3/library/collections.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc#collections.Counter


def read_to_file(path):
    with open(path, mode="r") as file_orders:
        dict_from_csv = csv.reader(file_orders)
        list_orders = []
        for order in enumerate(dict_from_csv):
            list_orders.append(order[1])

    return list_orders


print(analyze_log("data/orders_1.csv"))
