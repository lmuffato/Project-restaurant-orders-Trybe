import csv


def import_data(path):
    data = []

    with open(path, mode="r") as file:
        lists = csv.reader(file)

        for nome, comida, semana in lists:
            data.append({
                "nome": nome,
                "comida": comida,
                "semana": semana
            })
    return data


def most_requested_by_Maria(orders):
    most_frequent_eat = orders[0]['comida']
    frequency = {}

    for order in orders:
        if order['nome'] == 'maria':
            if order['comida'] not in frequency:
                frequency[order['comida']] = 1
            else:
                frequency[order['comida']] += 1
            if frequency[order['comida']] > frequency[most_frequent_eat]:
                most_frequent_eat = order['comida']

    return most_frequent_eat


def how_many_by_Arnaldo(orders):
    result = 0

    for order in orders:
        if order['nome'] == 'arnaldo':
            if order['comida'] == 'hamburguer':
                result += 1
    return str(result)


def never_asked_by_Joao(orders):
    joao_eats = []
    all_eats = []

    for order in orders:
        if order['nome'] == 'joao':
            joao_eats.append(order['comida'])
        else:
            all_eats.append(order['comida'])

    joao_eats_set = set(joao_eats)
    all_eats_set = set(all_eats)

    return all_eats_set.difference(joao_eats_set)


def never_weeks_by_Joao(orders):
    joao_weeks = []
    all_weeks = []

    for order in orders:
        if order['nome'] == 'joao':
            joao_weeks.append(order['semana'])
        else:
            all_weeks.append(order['semana'])

    joao_weeks_set = set(joao_weeks)
    all_weeks_set = set(all_weeks)

    return all_weeks_set.difference(joao_weeks_set)


def write_data(most_request, how_many, never_asked, never_weeks):
    with open('data/mkt_campaign.txt', "w") as file:
        file.write(f"{most_request}\n")
        file.write(f"{how_many}\n")
        file.write(f"{never_asked}\n")
        file.write(f"{never_weeks}\n")


def analyze_log(path_to_file):
    data = import_data(path_to_file)
    most_requested = most_requested_by_Maria(data)
    how_many = how_many_by_Arnaldo(data)
    never_asked = never_asked_by_Joao(data)
    never_weeks = never_weeks_by_Joao(data)
    write_data(most_requested, how_many, never_asked, never_weeks)
