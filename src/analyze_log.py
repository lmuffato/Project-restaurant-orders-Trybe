import csv
from collections import Counter


def read_csv(path_to_file):
    with open(path_to_file, 'r') as file:
        keys = ["customer", "order", "weekday"]
        reader = csv.DictReader(file, fieldnames=keys)
        data = [data for data in reader]
        return data


def person_filter(data, person):
    filtered_data = [d for d in data if d['customer'] == person]
    return filtered_data

def most_ordered_dish(data):
    filtered_data = [d['order'] for d in data]
    count = Counter(filtered_data)
    return count.most_common(1)[0][0]
  
def count_order(data, dish):
    filtered_data = [d['order'] for d in data if d['order']== dish]
    count = Counter(filtered_data)
    return count.get(dish)

def dishes_never_ordered(data,customer_data):
    filtered_data = [d['order'] for d in data]
    custumer_filter = [d['order'] for d in customer_data]
    return (set(filtered_data)-set(custumer_filter))
  
def absent_days(data,customer_data):
    filtered_data = [d['weekday'] for d in data]
    custumer_filter = [d['weekday'] for d in customer_data]
    return (set(filtered_data)-set(custumer_filter))

def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    log = []
    
    maria_data = person_filter(data, 'maria')
    maria_most_ordered = most_ordered_dish(maria_data)
    
    arnaldo_data = person_filter(data, 'arnaldo')
    arnaldo_ordered = count_order(arnaldo_data, 'misto-quente')
    
    joao_data = person_filter(data, 'joao')
    dishes = dishes_never_ordered(data, joao_data)
    days = absent_days(data, joao_data)

    return days

print(analyze_log('data/orders_1.csv'))
