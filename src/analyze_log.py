import csv
from collections import Counter

# a funcao list() coloca os dados do arq csv em uma lista
def readFile(path_to_file):
    with open(path_to_file, mode="r") as file:
        data = csv.DictReader(file, fieldnames=['customer', 'meal', 'day'])
        # for row in data:
            # print(row['customer'], row['meal'], row['day'])
        return list(data)


def number_of_meals(data):
    meals_list = []
    for row in data:
        if row['customer'] == 'maria':
            meals_list.append(row['meal'])
    c = Counter(meals_list)
    a_mais_pedida = c.most_common(1)[0][0]
    return a_mais_pedida

def num_hamburguer(data):
    meals_list = []
    for row in data:
        if row['customer'] == 'arnaldo':
            meals_list.append(row['meal'])
    c = Counter(meals_list)['hamburguer'] 
    return c

def never_ordered(data):
    meals_list = []
    all_meals = []
    for row in data:
        all_meals.append(row['meal'])
        if row['customer'] == 'joao':
            meals_list.append(row['meal'])
    
    e = set(all_meals)
    c = set(meals_list)
    return e.difference(c)

def never_there(data):
    all_days = []
    johns_day = []
    for row in data:
        all_days.append(row['day'])
        if row['customer'] == 'joao':
            johns_day.append(row['day'])

    a = set(all_days)
    b = set(johns_day)
    return a.difference(b)

def analyze_log(path_to_file):
    data = readFile(path_to_file)
    maria_meals = number_of_meals(data)
    joao_melao = num_hamburguer(data)
    hamburgueiro = never_ordered(data)
    terca = never_there(data)

    with open('data/mkt_campaign.txt', mode="w") as file:
       file.write(maria_meals + "\n")
       file.write(str(joao_melao) + "\n")
       file.write(str(hamburgueiro) + "\n")
       file.write(str(terca))

analyze_log('data/orders_1.csv')