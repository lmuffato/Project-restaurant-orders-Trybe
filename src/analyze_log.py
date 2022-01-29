import csv
from collections import Counter


# Código de leitura que eu mesmo criei no arquivo jobs.py do meu projeto
# Job Insights. Link: https://github.com/tryber/sd-010-a-project-
# job-insights/blob/carlos25xrm-job-insights/src/jobs.py
def leitura(path_to_file):
    with open(path_to_file, mode='r') as pedidos1:
        dados = []
        dados_lidos = csv.DictReader(pedidos1)
        for elemento in dados_lidos:
            dados.append(elemento)
    return dados


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
    raise NotImplementedError
