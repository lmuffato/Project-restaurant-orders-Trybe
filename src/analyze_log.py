import csv


def read_file(path_to_file):
    orders = []
    with open(path_to_file, mode="r") as file:
        file = csv.reader(file)
        for order in file:
            orders.append(order)
    return orders


def orders_by_name(orders, customer):
    name_orders = []
    for order in orders:
        if order[0] == customer:
            name_orders.append([order[1], order[2]])

    return name_orders


def get_most_ordered_meal(orders, customer):
    count = {}
    marias_orders = []

    marias_orders = orders_by_name(orders, customer)
    print(marias_orders)
    marias_most_ordered = marias_orders[0][0]
    for order in marias_orders:
        if order[0] not in count:
            count[order[0]] = 1
        else:
            count[order[0]] += 1

        if count[order[0]] > count[marias_most_ordered]:

            marias_most_ordered: order[0]

    return marias_most_ordered


def get_times_arnaldo_got_hamburguer(orders):
    arnaldo_orders = []
    for order in orders:
        if order[0] == 'arnaldo':
            arnaldo_orders.append([order[1], order[2]])

    count = {}

    for meal, day in arnaldo_orders:
        if meal not in count:
            count[meal] = 1
        else:
            count[meal] += 1
    return count['hamburguer']


def get_meals_never_order(orders, customer):
    all_meals = set()
    joao_ordered_meals = set()

    for order in orders:
        if order[0] == customer:
            joao_ordered_meals.add(order[1])
        else:
            all_meals.add(order[1])

    return all_meals.symmetric_difference(joao_ordered_meals)


def get_days_didnt_order(orders, costumer):
    all_days = set()
    days_joao_went = set()

    for order in orders:
        if order[0] == costumer:
            days_joao_went.add(order[2])
        else:
            all_days.add(order[2])

    return all_days - days_joao_went


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    marias_most_ordered_meal = get_most_ordered_meal(orders, 'maria')
    times_arnaldo_got_hamburguer = get_times_arnaldo_got_hamburguer(orders)
    meals_joao_never_order = get_meals_never_order(orders, 'joao')
    days_joao_didnt_order = get_days_didnt_order(orders, 'joao')

    output = f"""{marias_most_ordered_meal}
{times_arnaldo_got_hamburguer}
{meals_joao_never_order}
{days_joao_didnt_order}"""

    file = open("data/mkt_campaign.txt", mode="w")
    file.write(output)
    file.close()


analyze_log("data/orders_1.csv")
