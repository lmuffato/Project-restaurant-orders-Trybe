import csv


def read_file(path_to_file):
    orders = {}
    with open(path_to_file, mode="r") as file:
        file = csv.reader(file)
        for name, meal, day in file:
            if name not in orders:
                orders[name] = []
            orders[name].append((meal, day))

    return orders


def get_marias_most_ordered_meal(orders):
    maria_orders = orders['maria']

    count = {}
    most_ordered = maria_orders[0][0]

    for meal, day in maria_orders:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1

        if count[meal] > count[most_ordered]:
            most_ordered: meal

    return most_ordered


def get_times_arnaldo_got_hamburguer(all_orders):
    arnaldo_orders = all_orders['arnaldo']

    count = {}

    for meal, day in arnaldo_orders:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1

    return count['hamburguer']


def get_meals_joao_never_order(orders):
    all_meals = set()
    joao_ordered_meals = set()

    for order in orders:
        if 'joao' in order:
            joao_ordered_meals.add(order[1])
        else:
            all_meals.add(order[1])

    return all_meals.symmetric_difference(joao_ordered_meals)


def get_days_joao_didnt_order(orders):
    all_days = set()
    days_joao_went = set()

    for order in orders:
        if 'joao' in order:
            days_joao_went.add(order[2])
        else:
            all_days.add(order[2])

    return all_days - days_joao_went


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    marias_most_ordered_meal = get_marias_most_ordered_meal(orders)
    times_arnaldo_got_hamburguer = get_times_arnaldo_got_hamburguer(orders)
    meals_joao_never_order = get_meals_joao_never_order(orders)
    days_joao_didnt_order = get_days_joao_didnt_order(orders)
    
    output = f"""{marias_most_ordered_meal}\n {times_arnaldo_got_hamburguer}\n
        {meals_joao_never_order}\n
        {days_joao_didnt_order}"""

    file = open("data/mkt_campaign.txt", mode="w")
    file.write(output)
    file.close()




def read_to_file(path):
    with open(path, mode="r") as file_orders:
        dict_from_csv = csv.reader(file_orders)
        list_orders = []
        for order in enumerate(dict_from_csv):
            list_orders.append(order[1])

    print(list_orders)

    read_to_file('data/orders_1.csv')