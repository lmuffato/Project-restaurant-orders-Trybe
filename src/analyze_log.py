import csv
from collections import Counter


def read_file(path):
    with open(path, newline="") as csvfile:
        columns = ["customer", "order", "day"]
        return list(csv.DictReader(csvfile, fieldnames=columns))


def get_customer_data(customer, data):
    return [item for item in data if item["customer"] == customer]


def get_most_ordered_food(data):
    orders = [order["order"] for order in data]
    count = Counter(orders)
    most_ordered = count.most_common(1)[0][0]
    return most_ordered


def get_days_never_been_at(customer_data, data):
    days_info = set([item["day"] for item in data])
    customer_info = set([item["day"] for item in customer_data])

    return days_info.difference(customer_info)


def get_order_quantity_customer(data, order):
    quantity = 0
    for item in data:
        if item["order"] == order:
            quantity += 1
    return quantity


def get_food_never_ordered(customer_data, data):
    orders = set([item["order"] for item in data])
    orders_customer = set([item["order"] for item in customer_data])

    return orders.difference(orders_customer)


def analyze_log(path):
    data = read_file(path)

    data_arnaldo = get_customer_data("arnaldo", data)
    data_maria = get_customer_data("maria", data)
    data_joao = get_customer_data("joao", data)

    column1 = get_most_ordered_food(data_maria)
    column2 = get_order_quantity_customer(data_arnaldo, "hamburguer")
    column3 = get_food_never_ordered(data_joao, data)
    column4 = get_days_never_been_at(data_joao, data)

    path = "data/mkt_campaign.txt"
    with open(path, "w") as file:
        for item in [column1, column2, column3, column4]:
            file.write(str(item) + "\n")
