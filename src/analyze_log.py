import csv


def csv_import(path_to_file):
    if path_to_file.endswith('csv'):
        with open(path_to_file) as file:
            return list(csv.reader(file, delimiter=","))
    else:
        raise FileNotFoundError(f'File not found: {path_to_file}')


def find_most_requested_food_by_client(data, client_name):
    foods = []
    for item in data:
        if item[0] == client_name:
            foods.append(item[1])
    
    return max(set(foods), key=foods.count)

# def how_many_times_requested_food(data, food, client_name):


def analyze_log(path_to_file):
    data = csv_import(path_to_file)
    most_requested_food = find_most_requested_food_by_client(data, 'maria')
    # print(most_requested_food)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(most_requested_food)
    # return data


# print(analyze_log('data/orders_1.csv'))
# analyze_log('data/orders_1.csv')
