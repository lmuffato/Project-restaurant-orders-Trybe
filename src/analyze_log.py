import csv


def reade_file_csv(path):
    with open(path) as file:
        data = csv.reader(file)
        return [(cust, order, day) for cust, order, day in data]


def get_order_max_purchased(data, person):
    food_init = data[0][1]
    list = {}
    for cust, order, day in data:
        if cust == person and order not in list:
            list[order] = 1
        elif cust == person and order in list:
            list[order] += 1

        if cust == person and list[order] > list[food_init]:
            food_init = order

    return food_init
    # return max(list, key=list.get)


def get_order_quantity(data, person, food):
    list = {}
    for cust, order, day in data:
        if cust == person and order not in list:
            list[order] = 1
        elif cust == person and order in list:
            list[order] += 1

    if food not in list:
        return 0

    return list[food]


def get_order_never_costumer(data, person):
    list = set()
    list_order_person = set()

    for cost, order, day in data:
        list.add(order)
        if cost == person:
            list_order_person.add(order)

    return list.difference(list_order_person)


def get_days_never_costumer(data, person):
    list_days = set()
    list_days_person = set()

    for cust, order, day in data:
        list_days.add(day)
        if cust == person:
            list_days_person.add(day)
    return list_days.difference(list_days_person)


def analyze_log(path_to_file):
    data = reade_file_csv(path_to_file)
    order_max_purchased = get_order_max_purchased(data, 'maria'),
    order_quantity = get_order_quantity(data, 'arnaldo', 'hamburguer'),
    order_never_costumer = get_order_never_costumer(data, 'joao'),
    days_never_costumer = get_days_never_costumer(data, 'joao')
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            f'{order_max_purchased[0]}\n',
            f'{order_quantity[0]}\n',
            f'{order_never_costumer[0]}\n',
            f'{days_never_costumer}'
        ])
