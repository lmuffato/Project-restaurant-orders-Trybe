import csv


def convert_log(path):
    with open(path) as file:
        return list(csv.DictReader(
            file, fieldnames=['client', 'orders', 'day']))


def filter_by_client(orders, client):
    return [order for order in orders if order['client'] == client]


def find_most_ordered_dish_by_maria(data, client):
    count = {}
    most_ordered = data[0]['orders']
    client_order = filter_by_client(data, client)

    for item in data:
        if item['client'] == client_order:
            if item['orders'] not in count:
                count[item['orders']] = 1
            else:
                count[item['orders']] += 1

            if count[item['orders']] > count[most_ordered]:
                most_ordered = item['orders']

    return most_ordered


def find_arnaldo_orders(data, client):
    client_order = filter_by_client(data, client)
    count = 0
    for item in client_order:
        if item['orders'] == 'hamburguer':
            count += 1
    return count


def find_joao_differences(data, client):
    client_order = filter_by_client(data, client)
    orders = set([client['orders'] for client in data])
    ordered = set([client['orders'] for client in client_order])

    days = set([client['day'] for client in data])
    days_by_client = set([client['day'] for client in client_order])

    return (orders.difference(ordered), days.difference(days_by_client))


def analyze_log(path_to_file):
    data = convert_log(path_to_file)
    most_ordered_dish_by_maria = find_most_ordered_dish_by_maria(data, "maria")
    arnaldo_orders = find_arnaldo_orders(data, "arnaldo")
    (not_ordered_by_joao, not_visited_by_joao) = find_joao_differences(
        data, "joao")
    methods = [
        most_ordered_dish_by_maria,
        arnaldo_orders,
        not_ordered_by_joao,
        not_visited_by_joao
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        for method in methods:
            file.write(f'{method}\n')
        file.close()
