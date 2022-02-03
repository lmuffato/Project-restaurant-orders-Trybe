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

def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as info_list:
        info_list.write(f'{maria_orders(path_to_file)}\n')