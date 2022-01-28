import csv


def csv_import(path_to_file):
    if path_to_file.endswith('csv'):
        with open(path_to_file) as file:
            return list(csv.reader(file, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")


def get_most_ordered_dish_per_costumer(data, costumer_name):
    foods = []
    for item in data:
        if item[0] == costumer_name:
            foods.append(item[1])

    return max(set(foods), key=foods.count)


def how_much_times_requested_dish(data, food, costumer_name):
    foods = []
    for item in data:
        if item[0] == costumer_name:
            if item[1] == food:
                foods.append(food)
    return len(foods)


def get_never_ordered_per_costumer(data, costumer_name):
    foods = set([food[1] for food in data])
    unique_foods = set(foods)
    for item in data:
        if item[0] == costumer_name:
            if item[1] in unique_foods:
                unique_foods.remove(item[1])
    return unique_foods


def get_days_never_visited_per_costumer(data, costumer_name):
    unique_days = set([day[2] for day in data])
    visited_days = set()
    for item in data:
        if item[0] == costumer_name:
            visited_days.add(item[2])
    return unique_days.difference(visited_days)


def analyze_log(path_to_file):
    data = csv_import(path_to_file)
    most_requested_dish = get_most_ordered_dish_per_costumer(data, 'maria')
    how_much_resquests = how_much_times_requested_dish(
        data, 'hamburguer', 'arnaldo')
    never_requested = get_never_ordered_per_costumer(data, 'joao')
    never_visited = get_days_never_visited_per_costumer(data, 'joao')
    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            f'{most_requested_dish}\n',
            f'{how_much_resquests}\n',
            f'{never_requested}\n',
            f'{never_visited}'])
