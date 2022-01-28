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


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        file_content = csv.DictReader(
            csv_file, fieldnames=('name', 'food', 'day'), delimiter=',')
        favorite_dash = get_favorite_dash(file_content, 'maria')

analyze_log('data/orders_1.csv')