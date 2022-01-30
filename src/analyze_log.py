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



def analyze_log(path_to_file):
    raise NotImplementedError

