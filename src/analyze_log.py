import csv


def read_csv(path):
    result = []
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            result.append({"cliente": row[0], "pedido": row[1], "dia": row[2]})
    return result


# filtra o arquivo por cliente
def filter_by_client(data, client):
    result = []
    for row in data:
        if row["cliente"] == client:
            result.append(row)
    return result


# conta o numero de pedidos por cliente
def count_elements(data):
    result = {pedido: data.count(pedido) for pedido in set(data)}
    return result


# retorna a quantidade de produtos pedidos por cliente
def request_by_client(data):
    result = []
    for row in data:
        result.append(row["pedido"])
    result = count_elements(result)
    return result


# retorna o produto mais pedido
def most_requested_product(data):
    result = []
    for row in data:
        result.append(row["pedido"])
    result = count_elements(result)
    result = max(result, key=result.get)
    return result


# retorna a lista de produtos
def products_list(data):
    result = []
    for row in data:
        result.append(row["pedido"])
    return result


# retorna um conjunto com os produtos que o cliente nunca pediu
def never_request_by_client(data, product_list):
    set_data = set(data)
    set_product_list = set(product_list)
    return set_product_list.difference(set_data)


# retorna todos os dias de todos os clientes
def get_all_days(data):
    result = []
    for row in data:
        result.append(row["dia"])
    return set(result)


# retorna os dias que o cliente pediu
def get_days_by_client(data):
    result = []
    for row in data:
        result.append(row["dia"])
    return set(result)


# retorna os dias que o cliente nunca fez pedidos
def get_days_never_go(all_days, days_by_client):
    return all_days.difference(days_by_client)


def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    products = products_list(data)
    all_days = get_all_days(data)
    maria = filter_by_client(data, "maria")
    arnaldo = filter_by_client(data, "arnaldo")
    joao = filter_by_client(data, "joao")
    joao_products = request_by_client(joao)
    joao_days = get_days_by_client(joao)

    most_requested_by_maria = most_requested_product(maria)
    hambuerguer_quantity_arnaldo = request_by_client(arnaldo)["hamburguer"]
    never_quested_by_joao = never_request_by_client(joao_products, products)

    with open("data/mkt_campaign.txt", mode='w') as file:
        file.write(f"{most_requested_by_maria}\n")
        file.write(f"{hambuerguer_quantity_arnaldo}\n")
        file.write(f"{never_quested_by_joao}\n")
        file.write(f"{get_days_never_go(all_days, joao_days)}")


analyze_log("./data/orders_1.csv")
