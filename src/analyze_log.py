import csv


def get_favorite_dash(file, name):
    food_dict = {}
    for row in file:
        if(row['name'] == name):
            if(row['food'] not in food_dict):
                food_dict[row['food']] = 1
            else:
                food_dict[row['food']] += 1
    return max(food_dict, key=food_dict.get)


def get_times_ordered_food(file, food, name):
    ordered_times = 0
    for row in file:
        if(row['name'] == name and row['food'] == food):
            ordered_times += 1
    return ordered_times


def get_dishes_never_ordered(file, name):
    dishes = {row['food'] for row in file}
    client_dishes = set([row['food'] for row in file if row['name'] == name])
    return client_dishes.symmetric_difference(dishes)


def get_days_dont_go_eat(file, name):
    days = {row['day'] for row in file}
    days_client_went = set([row['day'] for row in file if row['name'] == name])
    return days_client_went.symmetric_difference(days)


def file_reader(path):
    with open(path) as csv_file:
        file_content = csv.DictReader(
            csv_file, fieldnames=('name', 'food', 'day'))
        return list(file_content)


def write_data(path, data_array):
    with open(path, 'w+') as txt_file:
        for data in data_array:
            txt_file.write(f'{str(data)}\n')


def analyze_log(path):
    favorite_dash = get_favorite_dash(file_reader(path), 'maria')
    times_ordered_food = get_times_ordered_food(
        file_reader(path), 'hamburguer', 'arnaldo')
    dishes_never_ordered = get_dishes_never_ordered(
        file_reader(path), 'joao')
    days_person_dont_go_eat = get_days_dont_go_eat(
        file_reader(path), 'joao')

    write_data('data/mkt_campaign.txt', [favorite_dash, times_ordered_food,
               dishes_never_ordered, days_person_dont_go_eat])


analyze_log('data/orders_1.csv')
