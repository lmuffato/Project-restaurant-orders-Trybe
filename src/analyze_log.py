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


# Aprendi o ".format" no curso de Python do Curso em Vídeo (Gustavo Guanabara)
def analyze_log(path_to_file):
    with open('./data/mkt_campaign.txt', mode='w') as arquivo:
        arquivo.write('{} \n'.format(mais_pedido_de_maria(path_to_file)))
