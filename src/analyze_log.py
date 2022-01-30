import csv


def read(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        return [{
                  'client': row[0],
                  'order': row[1],
                  'day': row[2],
                } for row in reader]


def count_maria(list):
    count = {'hamburguer': 0, 'pizza': 0, 'coxinha': 0}
    max_fraquency = "hamburguer"

    for register in list:
        if register['client'] == 'maria':
            count[register['order']] += 1

            if count[register['order']] > count[max_fraquency]:
                max_fraquency = register['order']

    return max_fraquency


def count_arnaldo(list):
    count = 0

    for register in list:
        if register['client'] == 'arnaldo':
            if register['order'] == 'hamburguer':
                count += 1

    return count


def count_joao(list):
    orders = {}
    joao_orders = {}

    for register in list:
        if register['order'] not in orders:
            orders[register['order']] = True

        if register['client'] == 'joao':
            if register['order'] not in joao_orders:
                joao_orders[register['order']] = True

    return { order for order in orders if order not in joao_orders }


def count_days(list):
    days = {}
    joao_days = {}

    for register in list:
        if register['day'] not in days:
            days[register['day']] = True

        if register['client'] == 'joao':
            if register['day'] not in joao_days:
                joao_days[register['day']] = True

    return { day for day in days if day not in joao_days }


def analyze_log(path_to_file):
    raise NotImplementedError

