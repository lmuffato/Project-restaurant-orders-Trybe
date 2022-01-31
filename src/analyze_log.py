import csv


def csv_reader(path_to_file):
    with open(path_to_file, mode='r') as first_orders_csv:
        orders_csv = csv.reader(first_orders_csv)
        csv_to_list = list(orders_csv)
    return csv_to_list


def analyze_log(path_to_file):
    raise NotImplementedError
