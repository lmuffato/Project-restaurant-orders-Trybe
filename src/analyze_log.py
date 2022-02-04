from csv import DictReader
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as log:
        return list(DictReader(log, fieldnames=['client', 'order', 'day']))


print(read('data/orders_1.csv'))


def write(path, information):
    with open(path, "w") as analysis:
        for data in information:
            analysis.write(f'{data}\n')
        analysis.close()


def filter_order_by_client(list, client):
    results = []
    for row in list:
        client_ = row["client"]
        if client == client_:
            results.append(row)
    return results


def find_most_ordered_by_client(filteredList):
    ordered = dict()
    for row in filteredList:
        if row["order"] not in ordered:
            ordered[row["order"]] = 1
        else:
            ordered[row["order"]] += 1
    result = max(ordered, key=ordered.get)
    return result


def item_amount_ordered_by_client(filteredList, snack):
    result = 0
    for row in filteredList:
        if row["order"] == snack:
            result += 1
    return result


def find_item_not_ordered_by_client(list, filteredList):
    ordered_by_clients = set([row['order'] for row in list])
    ordered_by_client = set([row['order'] for row in filteredList])
    return ordered_by_clients.difference(ordered_by_client)


def find_day_never_frequented(list, filteredList):
    frequented_by_clients = set([row['day'] for row in list])
    frequented_by_client = set([row['day'] for row in filteredList])
    return frequented_by_clients.difference(frequented_by_client)


def analyze_log(path_to_file):
    log = read(path_to_file)
    Maria_orders = filter_order_by_client(log, 'maria')
    Maria_most_ordered = find_most_ordered_by_client(Maria_orders)
    Arnaldo_orders = filter_order_by_client(log, 'arnaldo')
    Arnaldo_ordered = item_amount_ordered_by_client(
        Arnaldo_orders, 'hamburguer'
    )
    Joao_orders = filter_order_by_client(log, 'joao')
    Joao_never_order = find_item_not_ordered_by_client(log, Joao_orders)
    Joao_never_goes = find_day_never_frequented(log, Joao_orders)

    data = []
    data.append(Maria_most_ordered)
    data.append(Arnaldo_ordered)
    data.append(Joao_never_order)
    data.append(Joao_never_goes)

    write('data/mkt_campaign.txt', data)
