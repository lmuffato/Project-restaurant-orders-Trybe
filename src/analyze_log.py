import csv
from collections import Counter


def read_csv(path_to_file):
    with open(path_to_file, 'r') as file:
        chaves = ["consumidor", "pedido", "dia_semana"]
        reader = csv.DictReader(file, fieldnames=chaves)
        # https://docs.python.org/3/library/csv.html uso do fieldnames
        # requisito feito com consulta do PR#3 e ajuda da Marília
        return [data for data in reader]


def person_filter(data, pessoa):
    pessoa_filtrada = [d for d in data if d['consumidor'] == pessoa]
    return pessoa_filtrada


def most_ordered_dish(data):
    pedido_filtrado = [d['pedido'] for d in data]
    count = Counter(pedido_filtrado)
    return count.most_common(1)[0][0]
    # https://www.kite.com/python/docs/collections.Counter.most_common
    # count retorna uma lista de tuplas. (1) pega o 1º pedido que mais aparece.
    # [0] pega a primeira tupla da lista contendo a chave com o nome do pedido
    # e o valor do numero de vezes que aparece
    # o segundo [0] pega a primeira posição da tupla e retorna apenas o nome do
    # pedido que mais aparece, "hamburger" por exemplo


def count_order(data, pedido):
    pedido_filtrado = [d['pedido'] for d in data if d['pedido'] == pedido]
    count = Counter(pedido_filtrado)
    return count[pedido]
    # https://www.guru99.com/python-counter-collections-example.html


def dishes_never_ordered(data, costumer_data):
    filtered_data = [d['pedido'] for d in data]
    custumer_filter = [d['pedido'] for d in costumer_data]
    filtered_data_set = set(filtered_data)
    custumer_filter_set = set(custumer_filter)
    dif = filtered_data_set.difference(custumer_filter_set)
    return dif


def absent_days(data, costumer_data):
    filtered_data = [d['dia_semana'] for d in data]
    custumer_filter = [d['dia_semana'] for d in costumer_data]
    filtered_data_set = set(filtered_data)
    custumer_filter_set = set(custumer_filter)
    dif = filtered_data_set.difference(custumer_filter_set)
    return dif


def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    log = []

    maria_data = person_filter(data, 'maria')
    maria_most_ordered = most_ordered_dish(maria_data)

    arnaldo_data = person_filter(data, 'arnaldo')
    arnaldo_ordered = count_order(arnaldo_data, 'hamburguer')

    joao_data = person_filter(data, 'joao')
    dishes = dishes_never_ordered(data, joao_data)
    days = absent_days(data, joao_data)

    log.extend([maria_most_ordered, arnaldo_ordered, dishes, days])

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in log:
            file.write(str(item) + '\n')
