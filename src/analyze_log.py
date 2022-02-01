import csv
from collections import Counter
# import os
# from pprint import pprint


def read_log(path):
    log = None

    with open(path, mode='r') as inp:
        reader = csv.reader(inp)
        log = [
            {"name": col[0], "food": col[1], "day": col[2]} for col in reader
        ]
    return log


def write_log(path, str_data):
    with open(path, mode='w') as op:
        op.write(str_data)


def get_all_days(log):
    return set([x["day"] for x in log])


def get_all_foods(log):
    return set([x["food"] for x in log])


def aggregate_person_by(name, key, log):
    return dict(Counter(
        [y[key] for y in [x for x in log if x["name"] == name]])
    )


def analyze_log(path):
    log = read_log(path)

    all_days = get_all_days(log)
    all_foods = get_all_foods(log)

    maria_food_agg = aggregate_person_by('maria', 'food', log)
    marias_most_asked_food = max(
        maria_food_agg, key=lambda x: maria_food_agg[x])

    arnaldo_food_agg = aggregate_person_by('arnaldo', 'food', log)
    arnaldo_hamburguer_many_orders = arnaldo_food_agg['hamburguer']

    joao_foods = set(aggregate_person_by('joao', 'food', log))
    joao_never_asked_foods = set.difference(all_foods, joao_foods)

    joao_days = set(aggregate_person_by('joao', 'day', log))
    joao_never_go_out_days = set.difference(all_days, joao_days)

    output = [
        marias_most_asked_food,
        arnaldo_hamburguer_many_orders,
        joao_never_asked_foods,
        joao_never_go_out_days
    ]

    write_log('data/mkt_campaign.txt', '\n'.join([str(x) for x in output]))


# analyze_log('data/orders_1.csv')
# print(read_log('data/orders_1.csv'))
