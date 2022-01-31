import collections
import csv


def import_csv(path):
    if path.endswith(".csv"):
        with open(path, "r") as csvfile:
            return list(csv.reader(csvfile, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def most_ordered_food_per_customer(csv_data, customer_name):
    list = []
    for order in csv_data:
        if order[0] == customer_name:
            list.append(order[1])
    return collections.Counter(list).most_common(1)[0][0]


def most_ordered_frequency_per_customer(csv_data, food, customer_name):
    list = []
    for order in csv_data:
        if order[0] == customer_name:
            if order[1] == food:
                list.append(food)
    return collections.Counter(list).most_common(1)[0][1]


def never_ordered_food_per_customer(csv_data, customer_name):
    list = set()
    customer_ordered = set()
    for order in csv_data:
        name = order[0]
        food = order[1]
        list.add(food)
        if name == customer_name:
            customer_ordered.add(food)
    return list.difference(customer_ordered)


def never_went_per_customer(csv_data, customer_name):
    days = set([day[2] for day in csv_data])
    visited = set()
    for day in csv_data:
        if day[0] == customer_name:
            visited.add(day[2])
    return days.difference(visited)


def analyze_log(path_to_file):
    csv_data = import_csv(path_to_file)
    food_per_customer = most_ordered_food_per_customer(csv_data, "maria")
    frequency_per_customer = most_ordered_frequency_per_customer(
        csv_data, "hamburguer", "arnaldo"
    )
    never_ordered_per_customer = never_ordered_food_per_customer(
        csv_data, "joao"
    )
    customer_never_went = never_went_per_customer(csv_data, "joao")
    with open("data/campaign.txt", "w") as f:
        f.write(f"{food_per_customer}\n")
        f.write(f"{frequency_per_customer}\n")
        f.write(f"{never_ordered_per_customer}\n")
        f.write(f"{customer_never_went}")
