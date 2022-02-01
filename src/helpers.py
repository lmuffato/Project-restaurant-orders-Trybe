from csv import reader


#função para ler o arquivo csv
def read_csv(path):
    array = []
    with open(path, "r") as file:
        add_array = reader(file, delimiter=",", quotechar='"')
        for row in add_array:
            customer, food, date = row
            array.append(
                {'customer': customer, 'food': food, 'date': date}
            )
    return array


# função que retorna qual prato mais pedido pelo cliente
def order_food(customer, orders):
    counter = {}
    most_requested_foods = ""
    orders_by_custumer = filter(lambda o: o['customer'] == customer, orders)

    for order in orders_by_custumer:
        is_food = order['food']
        if is_food not in counter:
            counter[is_food] = 1
        else:
            counter[is_food] += 1
        if most_requested_foods == "" or counter[is_food] > counter[most_requested_foods]:
            most_requested_foods = is_food

    return most_requested_foods
