import csv

all_foods = {"misto-quente", "hamburguer", "pizza", "coxinha"}
all_days = {"segunda-feira", "terça-feira", "sabado"}


def read_orders_file(path_to_file):
    all_orders = {}
    with open(path_to_file, mode="r") as my_file:
        my_file = csv.reader(my_file)
        for name, order, week_day in my_file:
            if name not in all_orders:
                all_orders[name] = []
            all_orders[name].append((order, week_day))

    return all_orders


def get_most_ordered_by_name(all_orders, person_name):
    person_orders = all_orders[person_name]

    count = {}
    most_ordered = person_orders[0][0]

    for name, day in person_orders:
        if name not in count:
            count[name] = 1
        else:
            count[name] += 1

        if count[name] > count[most_ordered]:
            most_ordered: name

    return most_ordered


def get_times_person_ordered_food(all_orders, person_name, order_name):
    person_orders = all_orders[person_name]

    count = {}

    for name, day in person_orders:
        if name not in count:
            count[name] = 1
        else:
            count[name] += 1

    return count[order_name]


def get_never_ordered_by_name(all_orders, person_name):
    person_orders = all_orders[person_name]
    ordered_by_person = set()

    for food, day in person_orders:
        ordered_by_person.add(food)

    return all_foods - ordered_by_person


def get_days_person_didnt_order(all_orders, person_name):
    person_orders = all_orders[person_name]
    days_person_go = set()

    for food, day in person_orders:
        days_person_go.add(day)

    return all_days - days_person_go


def analyze_log(path_to_file):
    all_orders = read_orders_file(path_to_file)
    most_ordered_by_maria = get_most_ordered_by_name(all_orders, "maria")
    hamburger_orders_by_arnaldo = get_times_person_ordered_food(
        all_orders, "arnaldo", "hamburguer"
    )
    never_ordered_joao = get_never_ordered_by_name(all_orders, "joao")
    days_joao_didnt_order = get_days_person_didnt_order(all_orders, "joao")

    output = f"""{most_ordered_by_maria}
{hamburger_orders_by_arnaldo}
{never_ordered_joao}
{days_joao_didnt_order}"""

    file = open("data/mkt_campaign.txt", mode="w")
    file.write(output)
    file.close()


analyze_log("data/orders_1.csv")
