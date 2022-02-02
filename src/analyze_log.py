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


def arnaldo_ordered_hamburguer(path_to_file):
    orders_csv = csv_reader(path_to_file)
    count_hamburguer = int(0)
    for index in range(len(orders_csv)):
        if (
            orders_csv[index][0] == 'arnaldo' and
            orders_csv[index][1] == 'hamburguer'
        ):
            count_hamburguer += 1
    return count_hamburguer


def joao_never_ordered(path_to_file):
    orders_csv = csv_reader(path_to_file)
    joao_orders = set()
    all_dishes = set()
    for index in range(len(orders_csv)):
        all_dishes.add(orders_csv[index][1])
        if orders_csv[index][0] == 'joao':
            joao_orders.add(orders_csv[index][1])
    return all_dishes.difference(joao_orders)


def days_joao_never_went(path_to_file):
    orders_csv = csv_reader(path_to_file)
    joao_went = set()
    all_days = set()
    for index in range(len(orders_csv)):
        all_days.add(orders_csv[index][2])
        if orders_csv[index][0] == 'joao':
            joao_went.add(orders_csv[index][2])
    return all_days.difference(joao_went)


def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as campaign_mkt:
        campaign_mkt.write(f'{maria_most_ordered(path_to_file)}\n')
        campaign_mkt.write(f'{arnaldo_ordered_hamburguer(path_to_file)}\n')
        campaign_mkt.write(f'{joao_never_ordered(path_to_file)}\n')
        campaign_mkt.write(f'{days_joao_never_went(path_to_file)}\n')
