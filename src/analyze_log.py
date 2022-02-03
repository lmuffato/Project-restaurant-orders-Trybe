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
    contador = Counter(pedido_filtrado)
    return contador[pedido]
    # https://www.guru99.com/python-counter-collections-example.html


def dishes_never_ordered(data, costumer_data):
    dados_filtrados = set([d['pedido'] for d in data])
    filtro_consumidor = set([d['pedido'] for d in costumer_data])
    dif = dados_filtrados.difference(filtro_consumidor)
    return dif


def absent_days(data, costumer_data):
    dados_filtrados = [d['dia_semana'] for d in data]
    custumer_filter = [d['dia_semana'] for d in costumer_data]
    dados_filtrados_set = set(dados_filtrados)
    filtro_consumidor_set = set(custumer_filter)
    dif = dados_filtrados_set.difference(filtro_consumidor_set)
    return dif


def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    log = []

    dados_maria = person_filter(data, 'maria')
    mais_pedido_maria = most_ordered_dish(dados_maria)

    dados_arnaldo = person_filter(data, 'arnaldo')
    pedidos_arnaldo = count_order(dados_arnaldo, 'hamburguer')

    dados_joao = person_filter(data, 'joao')
    pratos = dishes_never_ordered(data, dados_joao)
    dias = absent_days(data, dados_joao)

    log.extend([mais_pedido_maria, pedidos_arnaldo, pratos, dias])

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in log:
            file.write(str(item) + '\n')
