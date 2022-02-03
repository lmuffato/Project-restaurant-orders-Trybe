import csv


def read_file(path):
    with open(path, newline='') as read:
        return list(csv.DictReader(read, fieldnames=['name', 'order', 'day']))


def get_data_per_name(orders, name):
    return [order for order in orders if order['name'] == name]


def most_requested_dish(orders, name):
    person_order = get_data_per_name(orders, name)
    count = {}
    most_requested = person_order[0]['order']

    for order in orders:
        if order['order'] not in count:
            count[order['order']] = 1
        else:
            count[order['order']] += 1

        if count[order['order']] > count[most_requested]:
            most_requested = order['order']

    return most_requested


def how_many_hamburger_func(orders, name, order_name):
    person_order = get_data_per_name(orders, name)
    print(person_order)
    count = 0
    for order in person_order:
        if order['order'] == order_name:
            count += 1
    return count


def how_many_orders_func(orders, name):
    person_order = get_data_per_name(orders, name)

    all_orders = set([name['order'] for name in orders])
    unique_person_orders = set([name['order'] for name in person_order])

    return all_orders.difference(unique_person_orders)


def how_many_days_func(orders, name):
    person_order = get_data_per_name(orders, name)

    all_order_days = set([name['day'] for name in orders])
    person_days = set([name['day'] for name in person_order])

    return all_order_days.difference(person_days)


def write_file(path, orders):
    file = open(path, 'w')
    for name in orders:
        file.write(f'{name}\n')
    file.close()


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    most_requested = most_requested_dish(orders, 'maria')
    how_many_hamburger = how_many_hamburger_func(
        orders, 'arnaldo', 'hamburguer'
    )
    john_never_asked = how_many_orders_func(orders, 'joao')
    john_never_days = how_many_days_func(orders, 'joao')
    write_file('data/mkt_campaign.txt', [
        most_requested,
        how_many_hamburger,
        john_never_asked,
        john_never_days
    ])


print(analyze_log('data/orders_1.csv'))
