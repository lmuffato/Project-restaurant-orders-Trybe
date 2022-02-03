import csv
from collections import Counter


def reader_CSV(path_to_file):
    with open(path_to_file, mode='r') as orders_01:
        data = csv.reader(orders_01)
        result_read = list(data)
    return result_read


def maria_orders(path_to_file):
    data = reader_CSV(path_to_file)
    orders = []
    for i in range(len(data)):
        if data[i][0] == 'maria':
            orders.append(data[i][1])
    return list(Counter(orders))[0]


def arnaldo_orders(path_to_file):
    data = reader_CSV(path_to_file)
    quantity_burger = 0
    for i in range(len(data)):
        if (data[i][0] == 'arnaldo' and data[i][1] == 'hamburguer'):
            quantity_burger += 1
    return quantity_burger


def joao_never_asked(path_to_file):
    data = reader_CSV(path_to_file)
    joao_orders = set()
    all_orders = set()
    for i in range(len(data)):
        all_orders.add(data[i][1])
        if data[i][0] == 'joao':
            joao_orders.add(data[i][1])
    return all_orders.difference(joao_orders)


def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as info_list:
        info_list.write(f'{maria_orders(path_to_file)}\n')
        info_list.write(f'{arnaldo_orders(path_to_file)}\n')
        info_list.write(f'{joao_never_asked(path_to_file)}\n')
