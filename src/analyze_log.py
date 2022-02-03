import csv
import os
from typing import Counter


def check_format_file(file):
    # print(file[-4:] == '.csv')
    if not file.endswith('.csv') or not os.path.isfile(file):
        raise FileNotFoundError(f"No such file or directory: '{file}'")


def read_csv(file):
    with open(file, 'r') as csv_reader:
        content = csv.reader(csv_reader, delimiter=',')
        array_of_sales = [row for row in content]
    return array_of_sales


def most_ordered(person, file):
    orders = read_csv(file)
    client_order = []
    for order in orders:
        if order[0] == person:
            client_order.append(order[1])
    return Counter(client_order).most_common(1)[0][0]
# client_orders = [row[1] for row in orders if client == row[0]]


def qty_order_client(order, client, file):
    orders_db = read_csv(file)
    return len([sale[1] for sale in orders_db
        if client == sale[0] and
        order == sale[1]]
    )


def never_ordered_client(client, file):
    orders_db = read_csv(file)
    dishes = set([order[1] for order in orders_db])
    order_client = set([order[1] for order in orders_db if order[0] == client])
    return(dishes - order_client)


def never_showUp_client(client, file):
    orders_db = read_csv(file)
    days_of_week = set([order[2] for order in orders_db])
    client_weekDay = set(
        [order[2] for order in orders_db if order[0] == client]
    )
    return(days_of_week - client_weekDay)


def analyze_log(path_to_file):
    check_format_file(path_to_file)
    answer1 = most_ordered('maria', path_to_file)
    answer2 = qty_order_client('hamburguer', 'arnaldo', path_to_file)
    answer3 = never_ordered_client('joao', path_to_file)
    answer4 = never_showUp_client('joao', path_to_file)
    with open('data/mkt_campaign.txt', 'w') as mkt_campaign:
        mkt_campaign.write(
            f'{answer1}\n'
            f'{answer2}\n'
            f'{answer3}\n'
            f'{answer4}\n'
        )


# check_format_file('data/orders_1.csv')
# print(most_ordered('maria','data/orders_1.csv'))
# print(read_csv('data/orders_1.csv'))
# print(qty_order_client('hamburguer', 'arnaldo', 'data/orders_1.csv'))
# print(never_ordered_client('joao','data/orders_1.csv'))
# print(never_showUp_client('joao', 'data/orders_1.csv'))
# print(check_format_file('data/orders_3.csv'))
