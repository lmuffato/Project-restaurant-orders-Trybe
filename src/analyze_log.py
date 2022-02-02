import csv
from collections import Counter


def read(path_to_file):
    with open(path_to_file, mode='r') as orders:
        data = csv.reader(orders)
        res = list(data)
    return res


def MariaMoreOrders(path_to_file):
    data = read(path_to_file)
    mariasOrders = []
    for i in range(len(data)):
        if data[i][0] == 'maria':
            mariasOrders.append(data[i][1])
    return list(Counter(mariasOrders))[0]


def arnaldosBurguers(path_to_file):
    data = read(path_to_file)
    numBurger = int(0)
    for i in range(len(data)):
        if (data[i][0] == 'arnaldo' and data[i][1] == 'hamburguer'):
            numBurger += 1
    return numBurger


def JoaosOrders(path_to_file):
    data = read(path_to_file)
    orders = set()
    allMenu = set()
    for i in range(len(data)):
        allMenu.add(data[i][1])
        if data[i][0] == 'joao':
            orders.add(data[i][1])
    return allMenu.difference(orders)


def daysJoao(path_to_file):
    data = read(path_to_file)
    days = set()
    allDays = set()
    for i in range(len(data)):
        allDays.add(data[i][2])
        if data[i][0] == 'joao':
            days.add(data[i][2])
    return allDays.difference(days)


def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as doc:
        doc.write(f'{MariaMoreOrders(path_to_file)}\n')
        doc.write(f'{arnaldosBurguers(path_to_file)}\n')
        doc.write(f'{JoaosOrders(path_to_file)}\n')
        doc.write(f'{daysJoao(path_to_file)}\n')
