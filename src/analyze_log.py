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


def analyze_log(path_to_file):
    raise NotImplementedError
