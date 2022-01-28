import csv
import os


def read(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        return [row for row in reader]


#  Recebe um array de strings
def get_frequency(array):
    most_frequent = array[0]
    less_frequent = array[0]
    list_count = {}
    items = set()

    for element in array:
        if element not in list_count:
            list_count[element] = 1
        else:
            list_count[element] += 1

        if list_count[element] > list_count[most_frequent]:
            most_frequent = element

        if list_count[element] < list_count[less_frequent]:
            less_frequent = element

        items.add(element)

    return (list_count, most_frequent, less_frequent, items)


def check_path(path_to_file):
    if not path_to_file:
        raise FileNotFoundError("Arquivo inexistente")

    _, extension = os.path.splitext(path_to_file)

    if extension != ".csv":
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")


def get_data(csv_parsed):
    my_foods = {}
    my_days = {}
    names = set()
    dishes = set()
    days = set()

    for a, b, c in csv_parsed:
        if a not in my_foods:
            my_foods[a] = [b]
        else:
            my_foods[a].append(b)

        if a not in my_days:
            my_days[a] = [c]
        else:
            my_days[a].append(c)

        names.add(a)
        dishes.add(b)
        days.add(c)

    return (my_foods, my_days, names, dishes, days)


def analyze_log(path_to_file):
    check_path(path_to_file)
    csv_parsed = read(path_to_file)
    my_foods, my_days, _, dishes, days = get_data(csv_parsed)

    my_file = []

    item1 = get_frequency(my_foods['maria'])[1]
    item2 = str(get_frequency(my_foods['arnaldo'])[0]['hamburguer'])
    item3 = str(dishes - get_frequency(my_foods['joao'])[3])
    item4 = str(days - get_frequency(my_days['joao'])[3])

    my_file.append(item1+'\n')
    my_file.append(item2+'\n')
    my_file.append(item3+'\n')
    my_file.append(item4)

    with open("data/mkt_campaign.txt", "w") as namesFile:
        namesFile.writelines(my_file)


analyze_log('data/orders_1.csv')
