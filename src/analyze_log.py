import csv
from collections import Counter


def read_csv(path_to_file):
    with open(path_to_file, "r") as file:
        keys = ["customer", "eat", "week_day"]
        reader = csv.DictReader(file, fieldnames=keys)
        data = [data for data in reader]
        return data


def get_customer_data(data, customer):
    customer_data = []

    for order in data:
        if order["customer"] == customer:
            customer_data.append(order)
    return customer_data


def most_ordered_eat(data):
    total_eats = []

    for order in data:
        total_eats.append(order["eat"])

    count = Counter(total_eats)
    return count.most_common(1)[0][0]


def get_total_order_of_eat(data, eat):
    total_eat_counter = 0

    for order in data:
        if order["eat"] == eat:
            total_eat_counter += 1

    return 1


def get_eat_never_ordered(customer_data, data):
    all_eats = []
    customer_eats = []

    for order in data:
        all_eats.append(order["eat"])

    for order in customer_data:
        customer_eats.append(order["eat"])

    return set(all_eats) - set(customer_eats)


def get_week_day_never_go(customer_data, data):
    all_days = []
    customer_days = []

    for order in data:
        all_days.append(order["week_day"])

    for order in customer_data:
        customer_days.append(order["week_day"])

    return set(all_days) - set(customer_days)


def analyze_log(path_to_file):
    csv_data = read_csv(path_to_file)

    maria_data = get_customer_data(csv_data, "maria")
    maria_most_ordered = most_ordered_eat(maria_data)

    arnaldo_data = get_customer_data(csv_data, "arnaldo")
    arnaldo_total_order = get_total_order_of_eat(arnaldo_data, "hamburguer")

    joao_data = get_customer_data(csv_data, "joao")
    joao_eat_never_ordered = get_eat_never_ordered(joao_data, csv_data)

    joao_never_week_day = get_week_day_never_go(joao_data, csv_data)

    with open("data/mkt_campaign.txt", mode="w") as text_file:
        text_file.write(str(maria_most_ordered) + "\n")
        text_file.write(str(arnaldo_total_order) + "\n")
        text_file.write(str(joao_eat_never_ordered) + "\n")
        text_file.write(str(joao_never_week_day) + "\n")

    print("teste")
