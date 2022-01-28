import csv


def read_file(path_to_file):
    with open(path_to_file) as file:
        data_reader = csv.reader(file)
        data = [data for data in data_reader]
        return data


def filter_by_customer(customer, data):
    customer_data = []

    for item in data:
        if customer in item:
            customer_data.append(item)

    return customer_data


def most_requested(data):
    request_counter = {}
    most_requested = data[0][1]

    for item in data:
        if item[1] in request_counter:
            request_counter[item[1]] += 1
        else:
            request_counter[item[1]] = 1

        if request_counter[item[1]] > request_counter[most_requested]:
            most_requested = request_counter[item[1]]

    return most_requested


def product_requestion_counter(product, data):
    counter = 0

    for item in data:
        if product in item:
            counter += 1

    return counter


def find_difference(customer_data, data):
    customer_requested = set()
    menu = set()

    for item in data:
        menu.add(item)

    for item in customer_data:
        customer_requested.add(item)

    return menu.difference(customer_requested)


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    results = []

    maria_data = filter_by_customer("maria", data)
    maria_most_requested = most_requested(maria_data)
    results.append(maria_most_requested)

    arnaldo_data = filter_by_customer("arnaldo", data)
    arnaldo_product_requestion = product_requestion_counter(
        "hamburguer", arnaldo_data
    )
    results.append(arnaldo_product_requestion)

    joao_data = filter_by_customer("joao", data)
    joao_never_requested = find_difference(
        [product[1] for product in joao_data], [product[1] for product in data]
    )
    results.append(joao_never_requested)

    joao_never_went = find_difference(
        [product[2] for product in joao_data], [product[2] for product in data]
    )
    results.append(joao_never_went)

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in results:
            file.write(str(item) + '\n')
