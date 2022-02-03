import csv
import os
from typing import Counter


def check_format_file(file):
    # print(file[:4] == '.csv')
    # print(file[4::])
    if not file.endswith('.csv') or not os.path.isfile(file):
        raise FileNotFoundError(f"No such file or directory: '{file}'")


def read_csv(file):
    with open(file, 'r') as csv_reader:
        content = csv.reader(csv_reader, delimiter=',')
        array_of_sales = [row for row in content]
    return array_of_sales
        
    
def most_ordered(person, file):
    orders = read_csv(file)
    client_order = []
    for order in orders:
        if order[0] == person:
            client_order.append(order[1])
    return Counter(client_order).most_common(1)[0][0]
# client_orders = [row[1] for row in orders if client == row[0]]


def analyze_log(path_to_file):
    check_format_file(path_to_file)
    most_ordered('maria', path_to_file)
    # raise NotImplementedError


check_format_file('data/orders_1.csv')
print(most_ordered('maria','data/orders_1.csv'))
