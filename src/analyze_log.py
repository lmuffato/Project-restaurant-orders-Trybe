import csv
import os


def read(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        return [row for row in reader]


def get_frequency(my_list):
    most_frequent = my_list[0]
    list_count = {}
    foods = set()

    for food in my_list:
        if food not in list_count:
            list_count[food] = 1
        else:
            list_count[food] += 1

        if list_count[food] > list_count[most_frequent]:
            list_count[most_frequent] = list_count[food]

        foods.add(food)

    return (list_count, most_frequent, foods)


def check_path(path_to_file):
    if not path_to_file:
        raise FileNotFoundError("Arquivo inexistente")

    _, extension = os.path.splitext(path_to_file)

    if extension != ".csv":
        raise FileNotFoundError("Extensão inválida")


def analyze_log(path_to_file):
    my_file = read(path_to_file)
    my_foods = {}
    my_days = {}
    names = set()
    dishes = set()
    days = set()

    for a, b, c in my_file:
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

    my_file = []

    item1 = get_frequency(my_foods['maria'])[1]
    item2 = str(get_frequency(my_foods['arnaldo'])[0]['hamburguer'])
    item3 = str(dishes - get_frequency(my_foods['joao'])[2])
    item4 = str(days - get_frequency(my_days['joao'])[2])

    my_file.append(item1+'\n')
    my_file.append(item2+'\n')
    my_file.append(item3+'\n')
    my_file.append(item4)

    with open("data/mkt_campaign.txt", "w") as namesFile:
        namesFile.writelines(my_file)
