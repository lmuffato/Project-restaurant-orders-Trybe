import csv


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        raw_data = csv.reader(file)
        data = [row for row in raw_data]
    most_ordered = orders_count(data, "maria")
    frequent_order = repeated_orders(data, "arnaldo", "hamburguer")
    never_ordered = not_ever_ordered(data, "joao")
    never_went = days_never_gone(data, "joao")

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(most_ordered) + '\n')
        file.write(str(frequent_order) + '\n')
        file.write(str(never_ordered) + '\n')
        file.write(str(never_went))


def orders_count(data, client):
    client_orders = []
    for row in data:
        if row[0] == client:
            client_orders.append(row[1])
    return max(client_orders, key=client_orders.count)


def repeated_orders(data, client, order):
    client_orders = 0
    for row in data:
        if row[0] == client and row[1] == order:
            client_orders += 1
    return client_orders


def not_ever_ordered(data, client):
    available_meals = []
    for row in data:
        if row[1] not in available_meals:
            available_meals.append(row[1])
    not_yet_ordered = available_meals
    for row in data:
        if row[0] == client and row[1] in not_yet_ordered:
            not_yet_ordered.remove(row[1])
    return not_yet_ordered


def days_never_gone(data, client):
    available_days = []
    for row in data:
        if row[2] not in available_days:
            available_days.append(row[2])
    not_yet_gone = available_days
    for row in data:
        if row[0] == client and row[2] in not_yet_gone:
            not_yet_gone.remove(row[2])
    return not_yet_gone


# hamburguer
# 1
# {'pizza', 'coxinha', 'misto-quente'}
# {'sabado', 'segunda-feira'}
