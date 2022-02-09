import csv


def read_path(path):
    with open(path) as file:
        return list(csv.reader(file, delimiter=","))


def orders(name, data):
    result = list()
    for customer in data:
        if customer[0] == name:
            result.append(customer[1])
    return max(set(result), key=result.count)


def hamburguer_orders(name, data):
    count = 0
    for customer in data:
        if customer[0] == name and customer[1] == "hamburguer":
            count += 1
    return count


def never_orders(name, data):
    customer_order = []
    recipes = []
    for row in data:
        recipes.append(row[1])
        if row[0] == name:
            customer_order.append(row[1])
    return set(recipes).symmetric_difference(set(customer_order))


def days(name, data):
    customer_order = []
    days = []
    for row in data:
        days.append(row[2])
        if row[0] == name:
            customer_order.append(row[2])
    return set(days).symmetric_difference(set(customer_order))


def analyze_log(path_to_file):
    data = read_path(path_to_file)
    maria_orders = orders("maria", data)
    arnaldo_hamburguer_orders = hamburguer_orders("arnaldo", data)
    joao = never_orders("joao", data)
    days_never_orders = days("joao", data)

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(
            [
                f"{maria_orders}\n",
                f"{arnaldo_hamburguer_orders}\n",
                f"{joao}\n",
                f"{days_never_orders}\n",
            ]
        )
