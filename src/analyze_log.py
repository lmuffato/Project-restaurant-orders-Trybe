import csv
from collections import Counter


def get_orders(path_to_file):
    with open(path_to_file, "r") as file:
        keys = ["customer", "order", "weekday"]
        order_data = csv.DictReader(file, fieldnames=keys)
        orders = []
        [orders.append(order) for order in order_data]
    return orders


def get_most_ordered_dish(customer, order_data):
    customer_order = [
        order["order"]
        for order in order_data
        if order["customer"] == customer
    ]
    count = Counter(customer_order)
    frequent = count.most_common(1)[0][0]
    return frequent


def get_quantity_by_dish(customer, dish, order_data):
    customer_order = [
        order["order"]
        for order in order_data
        if order["customer"] == customer
    ]
    count = Counter(customer_order)
    dish_count = count.get(dish)
    return dish_count


def get_dishes_without_orders(customer, order_data):
    menu = {orders["order"] for orders in order_data}
    customer_order = {
        order["order"]
        for order in order_data
        if order["customer"] == customer
    }
    # https://www.programiz.com/python-programming/methods/set/symmetric_difference
    dish_without_orders = menu.symmetric_difference(customer_order)
    return dish_without_orders


def get_absence_per_customer(customer, order_data):
    days_with_orders = {orders["weekday"] for orders in order_data}
    days_by_customer = {
        order["weekday"]
        for order in order_data
        if order["customer"] == customer
    }
    # https://www.programiz.com/python-programming/methods/set/symmetric_difference
    absence_days = days_with_orders.symmetric_difference(days_by_customer)
    return absence_days


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        path = "data/mkt_campaign.txt"
        order_data = get_orders(path_to_file)
        marias_favorite = get_most_ordered_dish("maria", order_data)
        arnaldos_hamburguers = get_quantity_by_dish(
            "arnaldo", "hamburguer", order_data
        )
        dishes_without_joao_orders = get_dishes_without_orders(
            "joao", order_data
        )
        days_without_joaos_presence = get_absence_per_customer(
            "joao", order_data
        )
        content = [
            f"{marias_favorite}\n",
            f"{arnaldos_hamburguers}\n",
            f"{dishes_without_joao_orders}\n",
            f"{days_without_joaos_presence}\n",
        ]
        with open(path, "w") as file:
            file.writelines(content)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
