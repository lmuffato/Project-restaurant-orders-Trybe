from functools import lru_cache
from typing import Counter
import csv

@lru_cache
def leitura(caminho):
    with open(caminho) as file: 
        requisicoes = csv.reader(file, limit=',')
        return [rows for rows in requisicoes]


def testeStr(path):
    requisicoes = []
    if (type(path) == str):
        requisicoes = leitura(path)
    else:
        requisicoes = path
    return requisicoes


def mariaPedidos(path):
    listaDerequisicoes = []
    testeString = testeStr(path)

    for requisicao in testeString:
        if(requisicao[0] == 'maria'):
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
    

def analyze_log(path_to_file):
    raise NotImplementedError
