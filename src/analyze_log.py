import csv
from typing import Counter

# Pesquisando o melhor jeito de contar items em lista: https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list

# Pesquisando como encontrar o maior número dentro de um dicionário: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary

def analyze_log(path_to_file):
    with open(path_to_file) as f:
        csv_opened_file = csv.DictReader(f, fieldnames=['name', 'food', 'weekday'])

        def person_favorite_meal(opened_file, person):
            person_orders = Counter(
                order['food'] for order in opened_file if order['name'] == person
            )

            return max(person_orders, key=person_orders.get) # estranho é que não precisa chamar a função dentro do key

        print(person_favorite_meal(csv_opened_file, 'arnaldo'))
        data_to_write = f"{person_favorite_meal(csv_opened_file, 'maria')}\n"
           
        

analyze_log('../data/orders_1.csv')
