import csv

# Import CSV to list. Ref:
# https://stackoverflow.com/questions/24662571/python-import-csv-to-list


def import_data(path_to_file):
    if path_to_file.endswith("csv"):
        with open(path_to_file) as file:
            csv_file = csv.reader(file, delimiter=",")
            return list(csv_file)
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")


def most_requested_dish_maria(data):
    maria_dishes = []

    for element in data:
        if element[0] == "maria":
            maria_dishes.append(element[1])
    # Ref. para como conseguir pegar o elemento com mais frequencia que foi
    # adicionado à lista maria_dishes:
    # https://www.geeksforgeeks.org/python-element-with-largest-frequency-in-list/
    return max(set(maria_dishes), key=maria_dishes.count)


def biggest_frequency_arnaldo_dish(data):
    counter = 0
    for element in data:
        if element[0] == 'arnaldo' and element[1] == 'hamburguer':
            counter += 1
    return counter


def never_ordered_joao(data):
    ordered_by_joao = []
    all_dishes = []

    for element in data:
        if element[0] == 'joao':
            ordered_by_joao.append(element[1])
        else:
            all_dishes.append(element[1])

    difference = set(all_dishes).difference(set(ordered_by_joao))
    return difference


def days_never_visited_joao(data):
    visited_days_joao = []
    all_work_days = []

    for element in data:
        if element[0] == 'joao':
            visited_days_joao.append(element[2])
        else:
            all_work_days.append(element[2])

    difference = set(all_work_days).difference(set(visited_days_joao))
    return difference


def analyze_log(path_to_file):
    data = import_data(path_to_file)
    most_requested = most_requested_dish_maria(data)
    biggest_frequency = biggest_frequency_arnaldo_dish(data)
    never_ordered = never_ordered_joao(data)
    never_visited_days = days_never_visited_joao(data)

    with open('data/mkt_campaign.txt', "w") as file:
        file.write(f"{most_requested}\n")
        file.write(f"{biggest_frequency}\n")
        file.write(f"{never_ordered}\n")
        file.write(f"{never_visited_days}\n")
    # raise NotImplementedError
