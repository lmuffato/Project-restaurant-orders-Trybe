import csv


def get_data(path):
    with open(path) as file:
        file_reader = csv.reader(file)
        data = [row for row in file_reader]

    return data


def get_unique_meals(path):
    with open(path) as file:
        file_reader = csv.reader(file)
        data = [row[1] for row in file_reader]

    return list(set(data))


def get_unique_days(path):
    with open(path) as file:
        file_reader = csv.reader(file)
        data = [row[2] for row in file_reader]

    return list(set(data))


def get_meal_count_by_person(path, person):
    meal_count = {}

    with open(path) as file:
        data = csv.reader(file)
        person_data = [row for row in data if row[0] == person]
        for row in person_data:
            if row[1] in meal_count:
                meal_count[row[1]] += 1
            else:
                meal_count[row[1]] = 1

    return meal_count


def analyze_log(path_to_file):
    unique_meals = get_unique_meals(path_to_file)
    unique_days = get_unique_days(path_to_file)
    meals_data = get_data(path_to_file)

    maria_meal_count = get_meal_count_by_person(path_to_file, 'maria')
    maria_most_ordered_meal = max(maria_meal_count, key=maria_meal_count.get)

    arnaldo_meal_count = get_meal_count_by_person(path_to_file, 'arnaldo')
    arnaldo_hamburger_orders = arnaldo_meal_count['hamburguer']

    joao_meal_count = get_meal_count_by_person(path_to_file, 'joao')

    joao_not_ordered_meals = set([
        meal for meal in unique_meals if meal not in joao_meal_count.keys()
    ])

    joao_meals = [meal for meal in meals_data if meal[0] == 'joao']
    joao_meal_days = [joao_meal[2] for joao_meal in joao_meals]
    joao_not_meal_days = set([
        day for day in unique_days if day not in joao_meal_days
    ])

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(maria_most_ordered_meal) + '\n')
        file.write(str(arnaldo_hamburger_orders) + '\n')
        file.write(str(joao_not_ordered_meals) + '\n')
        file.write(str(joao_not_meal_days))


if __name__ == '__main__':
    analyze_log('data/orders_1.csv')
