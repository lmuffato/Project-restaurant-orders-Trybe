import csv


# IMPORTAR DADOS DO ARQUIVO CSV
def get_data(path):
    with open(path) as file:  # abre o arquivo
        readed_file = csv.reader(file)  # lê o arquivo
        # converte em um array, contendo arrays
        # com as informações de cada linha
        data = [row for row in readed_file]
    return data


# Teste
# print(get_data('data/orders_1.csv'))


# RETORNAR REFEIÇÕES ÚNICAS
def get_unique_foods(data):
    # row[1] para selecionar o elemento da comida
    # Array típico: ['maria', 'hamburguer', 'terça-feira']
    data_foods = [element[1] for element in data]
    # set(array) -> Não retorna valores repetidos no array
    # o que transforma em um array de itens únicos
    unique_foods = set(data_foods)
    return list(unique_foods)

# Teste
# print(get_unique_foods(get_data('data/orders_1.csv')))


# RETORNAR DIAS ÚNICOS
def get_unique_days(data):
    days = [row[2] for row in data]
    unique_days = set(days)
    return list(unique_days)


# Teste
# print(get_unique_days(get_data('data/orders_1.csv')))


# RETORNAR A CONTAGEM DOS PEDIDOS POR PESSOA
def get_food_count_by_person(data, person):
  # Definindo conjunto de elementos distintos {}
  # O set(array) faz o mesmo, porém contendo dados
    food_count = {}

    # retornar apenas as linhas onde a pessoa for igual a person
    # o nome da pessoa está no index 0 da linha.
    person_info = [row for row in data if row[0] == person]
    # para cada linha em person_info
    for row in person_info:
        # se comida existir no set object
        if row[1] in food_count:
            # a chave com o nome da comida recebe mais 1
            food_count[row[1]] += 1
        else:
            # Se não existir a chave, cria ela e coloca 1
            food_count[row[1]] = 1

    return food_count


# Teste
# get_food_count_by_person('data/orders_1.csv', 'maria')
# print(get_food_count_by_person(get_data_from_csv('data/orders_1.csv'), 'maria'))


# O PRATO MAIS PEDIDO POR PESSOA
def most_requested_food_by_maria(data):
    maria_food_count = get_food_count_by_person(data, 'maria')
    maria_most_ordered_food = max(maria_food_count, key=maria_food_count.get)
    return maria_most_ordered_food


# QUANTAS VEZES ARNALDO PEDIU HAMBURGUER
def count_requested_hamburguer_by_arnaldo(data):
    arnaldo_food_count = get_food_count_by_person(data, 'arnaldo')
    arnaldo_hamburger_count = arnaldo_food_count['hamburguer']
    return arnaldo_hamburger_count


# COMIDA QUE O JOÃO NUNCA PEDIU
def food_joao_never_requested(data):
    unique_foods = get_unique_foods(data)
    joao_food_count = get_food_count_by_person(data, 'joao')
    food_joao_never_requested = set(
      [food for food in unique_foods if food not in joao_food_count.keys()]
    )
    return food_joao_never_requested


# DIAS QUE O JOÃO NUNCA FOI NA LANCHONETE
def days_that_john_never_went(data):
    unique_days = get_unique_days(data)

    # Filtra apenas os arrays em que o nome é 'joao'
    joao_foods = [food for food in data if food[0] == 'joao']

    joao_food_days = [joao_food[2] for joao_food in joao_foods]

    # retorna qual dia do joao, nao consta nos dias unicos
    joao_not_food_days = set([
        day for day in unique_days if day not in joao_food_days
    ])
    return joao_not_food_days


def analyze_log(path_to_file):
    data = get_data(path_to_file)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(most_requested_food_by_maria(data)) + '\n')
        file.write(str(count_requested_hamburguer_by_arnaldo(data)) + '\n')
        file.write(str(food_joao_never_requested(data)) + '\n')
        file.write(str(days_that_john_never_went(data)))


# Teste manual
# print(analyze_log('data/orders_1.csv'))


# Teste unitario
# python3 -m pytest tests/test_analyze_log.py
