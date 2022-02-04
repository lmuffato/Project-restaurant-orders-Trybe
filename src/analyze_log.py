import csv
from collections import Counter


def read_file(path):
    with open(path, newline="") as file:
        columns = ["customer", "order", "week_day"]
        return list(csv.DictReader(file, fieldnames=columns))


def get_customers_info(customer, data):
    return [item for item in data if item["customer"] == customer]


def find_most_ordered(data):
    orders = [order["order"] for order in data]
    count = Counter(orders)
    most_ordered = count.most_common(1)[0][0]
    return most_ordered


def find_unusual_days(customer_info, data):
    days = set([item["week_day"] for item in data])
    customer_days = set([item["week_day"] for item in customer_info])

    return days.difference(customer_days)


def count_custemer_order(data, order):
    total = 0
    for item in data:
        if item["order"] == order:
            total += 1
    return total


def find_never_ordered_food(customer_info, data):
    orders = set([item["order"] for item in data])
    customer_orders = set([item["order"] for item in customer_info])

    return orders.difference(customer_orders)


def analyze_log(path_to_file):
    raise NotImplementedError
