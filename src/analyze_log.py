import csv

def read(path_to_file):
    with open(path_to_file, mode='r') as orders:
        data = csv.reader(orders)
        res = list(data)
    return res


def analyze_log(path_to_file):
    raise NotImplementedError
