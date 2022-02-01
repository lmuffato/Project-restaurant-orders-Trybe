import csv
from collections import Counter


def csv_reader(path_to_file):
    with open(path_to_file, mode='r') as first_orders_csv:
        orders_csv = csv.reader(first_orders_csv)
        csv_to_list = list(orders_csv)
    return csv_to_list


def maria_most_ordered(path_to_file):
    orders_csv = csv_reader(path_to_file)
    marias_orders = []
    for index in range(len(orders_csv)):
        if orders_csv[index][0] == 'maria':
            marias_orders.append(orders_csv[index][1])
    return list(Counter(marias_orders))[0]


def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as campaign_mkt:
        campaign_mkt.write(f'{maria_most_ordered(path_to_file)}\n')
