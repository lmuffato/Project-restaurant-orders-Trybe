import csv
from collections import Counter


def read(path_to_file):
    with open(path_to_file, mode='r') as orders:
        data = csv.reader(orders)
        res = list(data)
    return res


def analyze_log(path_to_file):
    raise NotImplementedError


def MariaMoreOrders(path_to_file):
    data = read(path_to_file)
    mariasOrders = []
    for i in range(len(data)):
        if data[i][0] == 'maria':
            mariasOrders.append(data[i][1])
    return list(Counter(mariasOrders))[0]
