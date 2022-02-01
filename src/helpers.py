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


# função que retorna quantas vezes o pedido foi feito por determinado cliente
def counter_order(customer, food, orders):
    filter_orders = list(filter(lambda o: o['customer'] == customer
                                  and o['food'] == food, orders))
    return len(filter_orders)


# função que retorna qual prato nunca foi pedido
def food_never_ordered(customer, orders):
    all_foods = set()
    for order in orders:
        all_foods.add(order['food'])

    foods_ordered_by_customer = set()
    orders_by_custumer = filter(lambda o: o['customer'] == customer, orders)
    for order in orders_by_custumer:
        foods_ordered_by_customer.add(order['food'])

    return all_foods - foods_ordered_by_customer


# função para gravar os dados são preenchidos de forma correta no arquivo data/mkt_campaign.txt
def write_data(content):
    with open('data/mkt_campaign.txt', 'w') as data:
        data.writelines(content)
