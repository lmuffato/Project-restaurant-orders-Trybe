import csv
from src.vividict import Vividict


def analyze_log(path_to_file):
    orders = read_orders(path_to_file)

    foods = get_possible_values_by_key(orders, "foods")
    days = get_possible_values_by_key(orders, "days")

    maria_most_food = get_most_value_by_order(orders["maria"]["foods"])
    arnaldo_hamburguer_amount = orders["arnaldo"]["foods"]["hamburguer"]
    joao_never_food = get_never_value_by_person(orders["joao"]["foods"], foods)
    joao_never_days = get_never_value_by_person(orders["joao"]["days"], days)

    informations = [
        maria_most_food,
        arnaldo_hamburguer_amount,
        joao_never_food,
        joao_never_days,
    ]

    save_orders_informations(informations)


def read_orders(path_to_file):
    orders = parse_csv_file(path_to_file)
    orders_by_person = get_orders_by_person(orders)
    return orders_by_person


def parse_csv_file(path_to_file):
    try:
        if path_to_file.endswith(".csv") is not True:
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'"
            )

        with open(path_to_file, "r") as file:
            csvFile = csv.reader(file)
            return [lines for lines in csvFile]
    except FileNotFoundError:
        raise


def get_orders_by_person(orders):
    orders_by_person = Vividict()

    for order in orders:
        person = order[0]
        day = order[2]
        food = order[1]

        day_amount = parse_amount_to_int(orders_by_person[person]["days"][day])
        food_amount = parse_amount_to_int(
            orders_by_person[person]["foods"][food]
        )

        orders_by_person[person]["days"][day] = day_amount + 1
        orders_by_person[person]["foods"][food] = food_amount + 1

    return orders_by_person


def parse_amount_to_int(amount):
    return amount if type(amount) is int else 0


def get_possible_values_by_key(orders, key):
    possible_values = []

    for person in orders:
        possible_values = [*possible_values, *orders[person][key]]

    return list(set(possible_values))


def get_most_value_by_order(order):
    order_items = list(order.items())
    amount_items = [value[1] for value in order_items]
    index_greater_value = amount_items.index(max(amount_items))

    return order_items[index_greater_value][0]


def get_never_value_by_person(values_person, possible_values):
    return set(possible_values).difference(values_person)


def save_orders_informations(informations):
    text_informations = ""

    for information in informations:
        text_informations += str(information) + "\n"

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(text_informations)
