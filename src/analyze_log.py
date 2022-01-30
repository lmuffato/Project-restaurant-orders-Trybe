import csv
from typing import Counter

"""
Pesquisando o melhor jeito de contar items em lista:
https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list

Pesquisando como encontrar o maior número dentro de um dicionário:
https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
"""


def analyze_log(path_to_file):
    # necessária variável para manter os resultados, já que,
    # em algum segundo loop dentro de uma função que chame o csv_opened_file,
    # o arquivo já foi lido e fechado, o que resulta em um array vazio.
    maintained_list_of_objs = []
    with open(path_to_file) as f:
        csv_opened_file = csv.DictReader(
            f, fieldnames=["name", "food", "weekday"]
        )
        for line in csv_opened_file:
            maintained_list_of_objs.append(line)

        def final_answer():
            # - Qual o prato mais pedido por 'maria'?
            # - Quantas vezes 'arnaldo' pediu 'hamburguer'?
            # - Quais pratos 'joao' nunca pediu?
            # - Quais dias 'joao' nunca foi na lanchonete?
            functions_answers_order = [
                person_favorite_meal(maintained_list_of_objs, "maria"),
                person_how_many_ordered(
                    maintained_list_of_objs, "arnaldo", "hamburguer"
                ),
                person_never_ordered(maintained_list_of_objs, "joao"),
                person_not_ordered_days(maintained_list_of_objs, "joao"),
            ]
            with open("./data/mkt_campaign.txt", "w+") as answer:
                for index, funct in enumerate(functions_answers_order):
                    # just to remove trailing last line
                    if index == len(functions_answers_order) - 1:
                        answer.write(f"{funct}".rstrip())
                    else:
                        answer.write(f"{funct}\r")

    final_answer()


def person_favorite_meal(maintaned_list, person):
    person_orders = Counter(
        order["food"] for order in maintaned_list if order["name"] == person
    )
    # estranho é que não precisa chamar a função dentro do key
    return max(person_orders, key=person_orders.get)


def person_how_many_ordered(maintaned_list, person, meal):
    person_orders = Counter(
        order["food"]
        for order in maintaned_list
        if order["name"] == person and order["food"] == meal
    )
    return person_orders[meal]


def person_never_ordered(maintaned_list, person):
    person_ordered_meals = Counter(
        [order["food"] for order in maintaned_list if order["name"] == person]
    )

    every_ordered_meal = Counter([order["food"] for order in maintaned_list])

    list_difference = [
        meal for meal in every_ordered_meal if meal not in person_ordered_meals
    ]

    return set(list_difference)


def person_not_ordered_days(order_dict, person):

    every_ordered_days = Counter([order["weekday"] for order in order_dict])
    person_ordered_days = Counter(
        [order["weekday"] for order in order_dict if order["name"] == person]
    )

    list_difference = [
        day for day in every_ordered_days if day not in person_ordered_days
    ]

    return set(list_difference)


# analyze_log("../data/orders_1.csv")
