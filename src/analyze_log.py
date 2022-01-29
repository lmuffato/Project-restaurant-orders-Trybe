import csv
from typing import Counter

# Pesquisando o melhor jeito de contar items em lista: https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list

# Pesquisando como encontrar o maior número dentro de um dicionário: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary


def analyze_log(path_to_file):
    with open(path_to_file) as f:
        csv_opened_file = csv.DictReader(
            f, fieldnames=['name', 'food', 'weekday'])

        def person_favorite_meal(opened_file, person):
            person_orders = Counter(
                order['food'] for order in opened_file if order['name'] == person
            )
            # estranho é que não precisa chamar a função dentro do key
            return max(person_orders, key=person_orders.get)

        def person_how_many_ordered(opened_file, person, meal):
            person_orders = Counter(
                order['food'] for order in opened_file if order['name'] == person and order['food'] == meal
            )
            return person_orders[meal]


        def person_never_ordered(opened_file, person):
            person_ordered_meals = Counter([
                order['food'] for order in opened_file if order['name'] == person
            ])
            every_ordered_meal = Counter([order['food'] for order in opened_file])
            
            list_difference = [
                meal for meal in every_ordered_meal if meal not in person_ordered_meals]

            return f"1- {person_ordered_meals} 2- {every_ordered_meal}"

        print(person_never_ordered(csv_opened_file, 'joao'))

        def person_not_ordered_days(order_dict, person):

            every_ordered_days = Counter([order["weekday"] for order in order_dict])
            person_ordered_days = Counter([order["weekday"] for order in order_dict if order["name"] == person])

            # list_difference = [
            #     day for day in every_ordered_days if day not in person_ordered_days]

            return every_ordered_days


analyze_log('../data/orders_1.csv')
