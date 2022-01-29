import csv


def get_csv_file(path):
    result = []
    with open(path) as file:
        restaurant_list = csv.reader(file, delimiter=',')
        for product in restaurant_list:
            result.append(product)

    return result


def maria_most_ordered_food(foods):
    count = {}
    most_frequent = foods[0]

    for food in foods:
        if food not in count:
            count[food] = 1
        else:
            count[food] += 1

        if count[food] > count[most_frequent]:
            most_frequent = food

    return most_frequent


def maria_orders(orders):
    foods = []
    for order in orders:
        if order[0] == 'maria':
            foods.append(order[1])

    most_ordered = maria_most_ordered_food(foods)
    return most_ordered


def times_arnaldo_ordered_hamb(orders):
    count = 0
    for order in orders:
        if (
            order[0] == 'arnaldo'
            and order[1] == 'hamburguer'
        ):
            count += 1
    return count


def joao_never_ordered(all_foods, joao_foods):
    not_ordered = set()
    for foods in all_foods:
        if foods not in joao_foods:
            not_ordered.add(foods)

    return not_ordered


def joao_orders(orders):
    all_foods_repeted = []
    all_foods = []
    foods = []
    for order in orders:
        if order[0] == 'joao':
            foods.append(order[1])
        all_foods_repeted.append(order[1])

    for food in all_foods_repeted:
        if food not in all_foods:
            all_foods.append(food)
    never_ordered = joao_never_ordered(all_foods, foods)
    return never_ordered


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
    maria_most_ordered = maria_orders(csv_file)
    arnaldo_hamburguer = times_arnaldo_ordered_hamb(csv_file)
    never_ordered = joao_orders(csv_file)
    joao_days = days_joao(csv_file)
