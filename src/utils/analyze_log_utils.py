import csv


def read_file(path):
    with open(path, "r") as csvfile:
        columns = ["customer", "order", "day"]
        return list(csv.DictReader(csvfile, fieldnames=columns))


def write_file(path, data):
    with open(path, "w") as file:
        for item in data:
            file.write(str(item) + "\n")


def get_data_per_customer(customer, data):
    return [item for item in data if item["customer"] == customer]


def get_most_requested_dish_per_customer(data):
    count = {}
    most_ordered = data[0]["order"]
    for item in data:
        if item["order"] not in count:
            count[item["order"]] = 1
        else:
            count[item["order"]] += 1

        if count[item["order"]] > count[most_ordered]:
            most_ordered = item["order"]

    return most_ordered


def get_food_quantity_per_customer(data, food_name):
    order_quantity = 0
    for item in data:
        if item["order"] == food_name:
            order_quantity += 1
    return order_quantity


def get_dishes_did_never_order_customer(customer_data, data):
    orders_data = set([item["order"] for item in data])
    orders_customer = set([item["order"] for item in customer_data])

    return orders_data.difference(orders_customer)


def get_days_never_went_customer(customer_data, data):
    days_data = set([item["day"] for item in data])
    days_customer = set([item["day"] for item in customer_data])

    return days_data.difference(days_customer)
