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


def order_never_requested_by_customer(data, customer_filtered):
    general_order = set([item["order"] for item in data])
    customer_order = set([item["order"] for item in customer_filtered])

    return general_order.difference(customer_order)


def days_customer_never_went(data, customer_filtered):
    general_order = set([item["day"] for item in data])
    customer_order = set([item["day"] for item in customer_filtered])

    return general_order.difference(customer_order)


def write_log_file(log_data):
    path_file = "data/mkt_campaign.txt"

    with open(path_file, "w") as file:
        for item in log_data:
            file.write(str(item) + "\n")
    file.close()


def analyze_log(path_to_file):
    log_data = []

    data_order = read_csv_file(path_to_file)

    get_maria_order = filter_order_by_customer(data_order, "maria")
    most_ordered_by_maria = most_ordered_by_customer(get_maria_order)

    get_arnaldo_data = filter_order_by_customer(data_order, "arnaldo")
    ordered_by_arnaldo = count_by_order(get_arnaldo_data, "hamburguer")

    get_joao_data = filter_order_by_customer(data_order, "joao")
    ordered_never_requested_by_joao = (
        order_never_requested_by_customer(data_order, get_joao_data)
      )
    days_joao_didnt_go = days_customer_never_went(data_order, get_joao_data)

    log_data.extend([
      most_ordered_by_maria,
      ordered_by_arnaldo,
      ordered_never_requested_by_joao,
      days_joao_didnt_go
    ])

    write_log_file(log_data)

# Aprendi com essa explicação o entendimento da lib Counter:
# https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
# E sobre o usdo do most_common:
# https://www.delftstack.com/pt/howto/python/python-counter-most-common/
