import csv


def which_days_not_went(cliente, orders):
    orders_set = set()
    client_set = set()

    for order in orders:
        if order['cliente'] == cliente:
            client_set.add(order['dia'])
        orders_set.add(order['dia'])
    return orders_set.difference(client_set)


def which_menu_not_ordered(cliente, orders):
    orders_set = set()
    client_set = set()

    for order in orders:
        if order['cliente'] == cliente:
            client_set.add(order['pedido'])
        orders_set.add(order['pedido'])
    return orders_set.difference(client_set)


def many_times_ordered(cliente, pedido, orders):
    counter = 0

    for order in orders:
        client = order['cliente']
        ordered = order['pedido']
        if client == cliente and ordered == pedido:
            counter += 1
    return counter


def most_ordered(cliente, orders):
    order_count = {}
    most_frequent = orders[0]['pedido']

    for order in orders:
        pedido = order['pedido']
        if order['cliente'] == cliente:
            if pedido not in order_count:
                order_count[pedido] = 1
            else:
                order_count[pedido] += 1
            if (order_count[pedido] > order_count[most_frequent]):
                most_frequent = pedido
    return most_frequent


def analyze_log(path_to_file):
    orders = []
    file_to_save = 'data/mkt_campaign.txt'
    with open(path_to_file) as file:
        logs = csv.reader(file)
        for log in logs:
            orders.append({
                'cliente': log[0],
                'pedido': log[1],
                'dia': log[2],
            })

    most_ordered_by_maria = most_ordered('maria', orders)
    many_times_by_arnaldo = many_times_ordered('arnaldo', 'hamburguer', orders)
    which_menu_not_ordered_by_joao = which_menu_not_ordered('joao', orders)
    which_days_not_went_by_joao = which_days_not_went('joao', orders)

    file_to_save = open('data/mkt_campaign.txt', mode='w')
    file_to_save.write(f'{most_ordered_by_maria}\n')
    file_to_save.write(f'{many_times_by_arnaldo}\n')
    file_to_save.write(f'{which_menu_not_ordered_by_joao}\n')
    file_to_save.write(f'{which_days_not_went_by_joao}\n')
    file_to_save.close()
