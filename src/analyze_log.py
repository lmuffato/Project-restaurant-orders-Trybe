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


def analyze_log(path_to_file):
    data = convert_log(path_to_file)
    most_ordered_dish_by_maria = find_most_ordered_dish_by_maria(data, "maria")
    methods = [most_ordered_dish_by_maria]

    with open("data/mkt_campaign.txt", mode="w") as file:
        for method in methods:
            file.write(f'{method}\n')
        file.close()
