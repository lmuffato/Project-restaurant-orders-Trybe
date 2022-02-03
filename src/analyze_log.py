from .utils.utils_fuctions import (
    csv_reader,
    all_foods,
    all_days,
)


def maria_fav_food(orders):
    foods = {}
    biggest_quantity = 0
    fav_food = ''
    for order in orders:

        if order[0] not in foods:
            foods[order[0]] = 1
        else:
            foods[order[0]] += 1
        if foods[order[0]] > biggest_quantity:
            biggest_quantity = foods[order[0]]
            fav_food = order[0]
    return fav_food


def arnaldo_hamburguer_counter(orders, meal):
    counter = 0
    for order in orders:
        if order[0] == meal:
            counter += 1
    print('Arnaldo pediu hamburguer:', counter)
    return counter


# Para implementação dos requisitos de João, consultei os PRs #58
def joao_foods(orders):
    foods = set()
    for order in orders:
        if order[0] not in foods:
            foods.add(order[0])
    return foods


def joao_days(orders):
    days = set()
    for order in orders:
        if order[1] not in days:
            days.add(order[1])
    return days


def analyze_log(path_to_file):
    orders = csv_reader(path_to_file)

    # Verfifica comida mais pedida de Maria
    maria_fav_meal = maria_fav_food(orders["maria"])

    # Verifica quantidade de vezes que arnaldo pediu hamburguer
    arnaldo_burguer_counter = arnaldo_hamburguer_counter(
        orders["arnaldo"], "hamburguer"
    )

    # verifica pedidos de João, os pratos que nunca pediu
    orders_foods = all_foods("data/orders_1.csv")
    joao_orders_foods = joao_foods(orders["joao"])
    joao_no_orders_foods = orders_foods.difference(joao_orders_foods)
    print("orders_foods", orders_foods)
    print("joao_orders_foods", joao_orders_foods)
    print("joao_no_orders_foods", joao_no_orders_foods)

    # dias em que não pediu
    orders_days = all_days("data/orders_1.csv")
    joao_orders_days = joao_days(orders["joao"])
    joao_no_orders_days = orders_days.difference(joao_orders_days)
    print("orders_days", orders_days)
    print("joao_orders_days", joao_orders_days)
    print("joao_no_orders_days", joao_no_orders_days)

    content = [
        maria_fav_meal,
        arnaldo_burguer_counter,
        joao_no_orders_foods,
        joao_no_orders_days,
    ]

    with open("data/mkt_campaign.txt", "w") as file:
        for data in content:
            file.write(f"{str(data)}\n")


analyze_log("data/orders_1.csv")
