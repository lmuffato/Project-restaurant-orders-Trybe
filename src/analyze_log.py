from csv import DictReader
from collections import Counter

# https://www.geeksforgeeks.org/python-collections-module/#counters
# https://stackoverflow.com/questions/17039539/replace-fieldnames-when-using-dictreader


def csv_reader(path):
    with open(path, 'r') as file:
        keys = ["customer", "order", "day"]
        logs = DictReader(file, fieldnames=keys)
        list_of_logs = [log for log in logs]
        return list_of_logs


def get_customer_info(data, customer_name):
    return [log for log in data if log["customer"] == customer_name]


def get_most_ordered_food(data):
    # transforma todos os valores dos pedidos numa lista e conta-os
    orders = [log['order'] for log in data]
    count = Counter(orders)
    return count.most_common(1)[0][0]


def get_food_never_ordered_by_customer(data, customer_data):
    all_orders = set([log["order"] for log in data])
    customer_orders = set([log["order"] for log in customer_data])

    return all_orders.difference(customer_orders)


def count_order_by_food(data, food):
    return [log['order'] for log in data].count(food)


def get_days_not_visited_by_customer(data, customer_data):
    all_days = set([log["day"] for log in data])
    customer_days = set([log["day"] for log in customer_data])
    return all_days.difference(customer_days)


def analyze_log(path_to_file):
    data = csv_reader(path_to_file)
    list_to_file = []

    maria_data = get_customer_info(data, 'maria')
    more_requests_by_maria = get_most_ordered_food(maria_data)
    list_to_file.append(more_requests_by_maria)

    arnaldo_data = get_customer_info(data, 'arnaldo')
    arnaldo_hamburguer_count = count_order_by_food(arnaldo_data, 'hamburguer')
    list_to_file.append(arnaldo_hamburguer_count)

    joao_data = get_customer_info(data, 'joao')
    joao_never_ordered = get_food_never_ordered_by_customer(data, joao_data)
    list_to_file.append(joao_never_ordered)

    joao_did_not_visited = get_days_not_visited_by_customer(data, joao_data)
    list_to_file.append(joao_did_not_visited)

    with open('data/mkt_campaign.txt', "w") as file:
        for item in list_to_file:
            file.write(str(item)+'\n')
