import csv
from collections import Counter


# INFORMAÇÕES IMPORTANTES: dados[index][0] == "nome"
# dados[index][1] == "comida" / dados[index][2] == "dia"

# Convertar de CSV para LISTA em Python:
# https://www.delftstack.com/pt/howto/python/how-to-read-csv-to-list-in-python
def leitura(path_to_file):
    with open(path_to_file, mode='r') as pedidos1:
        dados = csv.reader(pedidos1)
        dados_lidos = list(dados)
    return dados_lidos


def mais_pedido_de_maria(path_to_file):
    dados = leitura(path_to_file)
    pedidos_de_maria = []
    for index in range(len(dados)):
        if dados[index][0] == 'maria':
            pedidos_de_maria.append(dados[index][1])
    mais_pedido = list(Counter(pedidos_de_maria))[0]
    return mais_pedido


def arnaldo_pediu_hamburguer(path_to_file):
    dados = leitura(path_to_file)
    quantos_hamburgueres = int(0)
    for index in range(len(dados)):
        if (dados[index][0] == 'arnaldo' and dados[index][1] == 'hamburguer'):
            quantos_hamburgueres += 1
    return quantos_hamburgueres


def pratos_joao_nunca_pediu(path_to_file):
    dados = leitura(path_to_file)
    todos_os_pratos = set()
    pratos_do_joao = set()
    for index in range(len(dados)):
        todos_os_pratos.add(dados[index][1])
        if dados[index][0] == 'joao':
            pratos_do_joao.add(dados[index][1])
    return todos_os_pratos.difference(pratos_do_joao)


# Aprendi o ".format" no curso de Python do Curso em Vídeo (Gustavo Guanabara)
def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as arquivo:
        arquivo.write('{} \n'.format(mais_pedido_de_maria(path_to_file)))
        arquivo.write('{} \n'.format(arnaldo_pediu_hamburguer(path_to_file)))
        arquivo.write('{} \n'.format(pratos_joao_nunca_pediu(path_to_file)))
