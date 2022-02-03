import csv


def get_csv_file(path):
    result = []
    with open(path) as file:
        restaurants = csv.reader(file, delimiter=',')
        for product in restaurants:
            result.append(product)
    return result


def get_most_ordered_food(foods):
    count_foods = {}
    most_frequent = foods[0]

    for food in foods:
        if food not in count_foods:
            count_foods[food] = 1
        else:
            count_foods[food] += 1

        if count_foods[food] > count_foods[most_frequent]:
            most_frequent = food

    return most_frequent


def maria_most_ordered_food(orders):
    foods = []
    for order in orders:
        if order[0] == 'maria':
            foods.append(order[1])
    most_ordered = get_most_ordered_food(foods)
    return most_ordered


def count_arnaldo_hamburguer(orders):
    count = 0
    for order in orders:
        if (
            order[0] == 'arnaldo'
            and order[1] == 'hamburguer'
        ):
            count += 1
    return count


def get_never_ordered_foods(all_foods, person_foods):
    not_ordered_foods = set()
    for foods in all_foods:
        if foods not in person_foods:
            not_ordered_foods.add(foods)
    return not_ordered_foods


def joao_never_ordered(orders):
    all_foods_repeted = []
    all_foods = []
    joao_foods = []
    for order in orders:
        if order[0] == 'joao':
            joao_foods.append(order[1])
        all_foods_repeted.append(order[1])

    for food in all_foods_repeted:
        if food not in all_foods:
            all_foods.append(food)
    never_ordered_foods = get_never_ordered_foods(all_foods, joao_foods)
    return never_ordered_foods


def joao_never_went(all_days, joao_days):
    never_went = set()
    for day in all_days:
        if day not in joao_days:
            never_went.add(day)
    return never_went


def days_joao(orders):
    all_days_repeated = []
    all_days = []
    joao_days = []
    for order in orders:
        if order[0] == 'joao':
            joao_days.append(order[2])
        all_days_repeated.append(order[2])

    for day in all_days_repeated:
        if day not in all_days:
            all_days.append(day)
    never_went = joao_never_went(all_days, joao_days)
    return never_went


def analyze_log(path_to_file):
    csv_file = get_csv_file(path_to_file)
    maria_most_ordered = maria_most_ordered_food(csv_file)
    arnaldo_hamburguer = count_arnaldo_hamburguer(csv_file)
    never_ordered = joao_never_ordered(csv_file)
    joao_days = days_joao(csv_file)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{maria_most_ordered}\n")
        file.write(f"{arnaldo_hamburguer}\n")
        file.write(f"{never_ordered}\n")
        file.write(f"{joao_days}")
