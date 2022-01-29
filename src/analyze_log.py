import csv


def csv_to_list(path):
    data = []
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            data.append({'client': row[0], 'order': row[1], 'day': row[2]})
    return data


def count_maria_order(list):
    count_order = {}
    most_frequent = list[0]['order']

    for register in list:
        if register['client'] == 'maria':
            if register['order'] not in count_order:
                count_order[register['order']] = 1
            else:
                count_order[register['order']] += 1
            if count_order[register['order']] > count_order[most_frequent]:
                most_frequent = register['order']

    return most_frequent


def count_arnaldo_hamburguer(list):
    count_ha = 0

    for register in list:
        if register['client'] == 'arnaldo' and register['order'
                                                        ] == 'hamburguer':
            count_ha += 1

    return count_ha


def count_joao_orders(list):
    all_orders = {}
    joao_orders = {}

    for register in list:
        if register['order'] not in all_orders:
            all_orders[register['order']] = True

        if register['client'] == 'joao':
            if register['order'] not in joao_orders:
                joao_orders[register['order']] = True

    return get_not_joao_orders(joao_orders, all_orders)


def get_not_joao_orders(joao_orders, all_orders):
    not_joao_orders = []
    for order in all_orders:
        if order not in joao_orders:
            not_joao_orders.append(order)

    return not_joao_orders


def count_joao_days(list):
    all_days = {}
    joao_days = {}

    for register in list:
        if register['day'] not in all_days:
            all_days[register['day']] = True

        if register['client'] == 'joao':
            if register['day'] not in joao_days:
                joao_days[register['day']] = True

    return get_not_joao_days(joao_days, all_days)


def get_not_joao_days(joao_days, all_days):
    not_joao_days = []
    for day in all_days:
        if day not in joao_days:
            not_joao_days.append(day)

    return not_joao_days


def analyze_log(path_to_file):
    list = csv_to_list(path_to_file)
    most_frequent_maria = count_maria_order(list)
    arnaldo_hamburguer = count_arnaldo_hamburguer(list)
    joao_not_ordered = count_joao_orders(list)
    joao_not_days = count_joao_days(list)
    file = open("data/mkt_campaign.txt", mode="w")

    file.write(str(most_frequent_maria)+"\n")
    file.write(str(arnaldo_hamburguer)+"\n")
    file.write(str(joao_not_ordered).replace('[', '{').replace(']', '}')+"\n")
    file.write(str(joao_not_days).replace('[', '{').replace(']', '}')+"\n")

    file.close()

# analyze_log('data/orders_1.csv')
