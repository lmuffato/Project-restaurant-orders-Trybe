from src.read_csv import ReadCsvFile


def get_max_order_client(orders, client):
    order_client = [order for order in orders if order["client"] == client]
    order_max = {}
    most_frequent = order_client[0]["order"]
    for order in order_client:
        food = order["order"]
        if food not in order_max:
            order_max[food] = 1
        else:
            order_max[food] += 1
        if order_max[food] > order_max[most_frequent]:
            most_frequent = food
    # print(most_frequent)
    return most_frequent


def get_order_client(orders, client, order):
    order_client = [order for order in orders if order["client"] == client]
    most = 0
    for order_item in order_client:
        if order_item["order"] == order:
            most += 1
    # print(most)
    return most


def get_not_ordered(orders, client):
    single_orders = {order["order"] for order in orders}
    order_client = (
        {order["order"] for order in orders if order["client"] == client})
    not_ordered = single_orders.difference(order_client)
    # print(not_ordered)
    return not_ordered


def get_not_days(orders, client):
    single_days = {order["day"] for order in orders}
    order_client = (
        {order["day"] for order in orders if order["client"] == client})
    not_days = single_days.difference(order_client)
    # print(not_days)
    return not_days


def analyze_log(path_to_file):
    order_list = ReadCsvFile.get_csv(path_to_file)

    get_max_order_maria = (
        get_max_order_client(order_list, "maria"))

    get_arnaldo_order_hamburguer = (
        get_order_client(order_list, "arnaldo", "hamburguer")
    )

    get_not_ordered_joao = (
        get_not_ordered(order_list, "joao")
    )

    get_not_days_joao = (
        get_not_days(order_list, "joao")
    )

    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines([
            f"{get_max_order_maria}\n"
            f"{str(get_arnaldo_order_hamburguer)}\n"
            f"{str(get_not_ordered_joao)}\n"
            f"{str(get_not_days_joao)}"])
