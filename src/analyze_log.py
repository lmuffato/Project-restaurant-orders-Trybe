import csv
from collections import Counter


def read_csv_file(path_to_file):
    with open(path_to_file) as file:
        dict_keys = ["customer", "order", "day"]

        reader = csv.DictReader(file, fieldnames=dict_keys)
        data = list(reader)
    return data


def filter_order_by_customer(data, customer):
    filtered_data = [item for item in data if item["customer"] == customer]

    return filtered_data


def most_ordered_by_customer(data):
    filtered_data = [item["order"] for item in data]
    count_order = Counter(filtered_data)

    return count_order.most_common(1)[0][0]


def count_by_order(data, order):
    filtered_data = [item["order"] for item in data if item["order"] == order]

    count_order = Counter(filtered_data)
    return count_order.get(order)


def analyze_log(path_to_file):

    data_order = read_csv_file(path_to_file)

    get_maria_order = filter_order_by_customer(data_order, "maria")
    most_ordered_by_maria = most_ordered_by_customer(get_maria_order)

    get_arnaldo_data = filter_order_by_customer(data_order, "arnaldo")
    ordered_by_arnaldo = count_by_order(get_arnaldo_data, "hamburguer")
    print(ordered_by_arnaldo)


# Aprendi com essa explicação o entendimento da lib Counter:
# https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
# E sobre o usdo do most_common:
# https://www.delftstack.com/pt/howto/python/python-counter-most-common/
