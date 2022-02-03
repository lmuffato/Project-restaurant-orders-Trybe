from functools import lru_cache
from typing import Counter
import csv


@lru_cache
def leitura(caminho):
    with open(caminho) as file:
        requisicoes = csv.reader(file, delimiter=',')
        return [rows for rows in requisicoes]


def testeStr(path):
    requisicoes = []
    if (type(path) == str):
        requisicoes = leitura(path)
    else:
        requisicoes = path
    return requisicoes


def mariaPedidos(path, cliente):
    listaDerequisicoes = []
    testeString = testeStr(path)

    for requisicao in testeString:
        if(requisicao[0] == cliente):
            listaDerequisicoes.append(requisicao[1])
    resposta = Counter(listaDerequisicoes).most_common(1)
    return resposta[0][0]


def quantHanburgueArnaldo(caminho):
    contador = 0
    testeString = testeStr(caminho)

    for requisicao in testeString:
        if(requisicao[0] == 'arnaldo' and requisicao[1] == 'hamburguer'):
            contador += 1
    return contador


def contadorNegativo(caminho, type, cliente):
    typeIndex = 0
    joaoItens = set()
    listItens = set()
    testeString = testeStr(caminho)

    if(type == 'plate'):
        typeIndex = 1
    if(type == 'day'):
        typeIndex = 2

    for requisicao in testeString:
        listItens.add(requisicao[typeIndex])
        if(requisicao[0] == cliente):
            joaoItens.add(requisicao[typeIndex])
    resposta = listItens.difference(joaoItens)
    return resposta


def analyze_log(caminho):
    maisPedidos = mariaPedidos(caminho)
    quantHanburgue = quantHanburgueArnaldo(caminho)
    contadorNeg = contadorNegativo(caminho, 'plate')
    diasFechados = contadorNegativo(caminho, 'day')

    file = open('data/mkt_campaign.txt', mode='w')
    file.writelines('{}\n{}\n{}\n{}\n'.format(
        maisPedidos, quantHanburgue, contadorNeg, diasFechados
    ))
    file.close
   