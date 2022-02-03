import csv

def reader_CSV(path_to_file):
    with open(path_to_file, mode='r') as orders_01:
        data = csv.reader(orders_01)
        result_read = list(data)
    return result_read

def analyze_log(path_to_file):
    raise NotImplementedError