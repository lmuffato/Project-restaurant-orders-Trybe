import csv
import os


def validate_file(file):
    message_error = 'No such file or directory: ' + "'" + file + "'"
    if not file.endswith('csv') or not os.path.isfile(file):
        raise FileNotFoundError(message_error)


def maria_dish(lists):
    count_dict = {}
    for row in lists:
        if 'maria' in row:
            try:
                count_dict[row[1]] += 1
            except KeyError:
                count_dict[row[1]] = 1
    max_dish = max(count_dict, key=count_dict.get)
    return max_dish


def arnaldo_burguer(lists):
    counter = 0
    for row in lists:
        if 'arnaldo' in row and 'hamburguer' in row:
            counter += 1
    return str(counter)


def joao_not_dishs(lists):
    return_list = []
    dishJoao = list(filter(lambda l: 'joao' in l, lists))
    dish_joao = list(map(lambda l: l[1], dishJoao))
    for row in lists:
        if 'joao' not in row and row[1] not in dish_joao:
            return_list.append(row[1])
    print(return_list)
    return set(return_list)


def joao_not_days(lists):
    return_list = []
    daysJoao = list(filter(lambda l: 'joao' in l, lists))
    days_joao = list(map(lambda l: l[2], daysJoao))
    for row in lists:
        if 'joao' not in row and row[2] not in days_joao:
            return_list.append(row[2])
    return set(return_list)


def analyze_log(path_to_file):
    validate_file(path_to_file)
    lines = []
    with open(path_to_file, 'r') as file:
        readed = csv.reader(file)
        rows_list = list(readed)
        lines.append(maria_dish(rows_list))
        lines.append(arnaldo_burguer(rows_list))
        lines.append(joao_not_dishs(rows_list))
        lines.append(joao_not_days(rows_list))
    with open('data/mkt_campaign.txt', 'w') as archive:
        for line in lines:
            archive.write(f"{line}\n")
