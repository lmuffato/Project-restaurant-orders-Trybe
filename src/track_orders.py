import csv
from collections import Counter
import os
from pprint import pprint

# def read_log(path):
#     log = None
    
#     with open(path, mode='r') as inp:
#         reader = csv.reader(inp)
#         log = [
#             {"name":col[0], "food": col[1], "day": col[2]} for col in reader
#         ]
#     return log

# def write_log(path, str_data):
#     with open(path, mode='w') as op:
#         op.write(str_data)

# def get_all_days(log):
#     return set([x["day"] for x in log])

# def get_all_foods(log):
#     return set([x["order"] for x in log])

# def aggregate_person_by(customer, key, log):
#     return dict(Counter(
#         [y[key] for y in==customer]])
#     ) [x for x in log if x["customer"]

# def analyze_log(path):
#     log = read_log(path)

#     all_days = get_all_days(log)
#     all_foods = get_all_foods(log)

#     maria_food_agg = aggregate_person_by('maria', 'food', log)
#     marias_most_asked_food = max(maria_food_agg, key = lambda x: maria_food_agg[x])

#     arnaldo_food_agg = aggregate_person_by('arnaldo', 'food', log)
#     arnaldo_hamburguer_many_orders = arnaldo_food_agg['hamburguer']

#     joao_foods = set(aggregate_person_by('joao', 'food', log))
#     joao_never_asked_foods = set.difference(all_foods, joao_foods)

#     joao_days = set(aggregate_person_by('joao', 'day', log))
#     joao_never_go_out_days = set.difference(all_days, joao_days)

#     output = [
#         marias_most_asked_food,
#         arnaldo_hamburguer_many_orders,
#         joao_never_asked_foods,
#         joao_never_go_out_days
#     ]

#     write_log('data/mkt_campaign.txt', '\n'.join([str(x) for x in output]))


# analyze_log('data/orders_1.csv')
# print(read_log('data/orders_1.csv'))


class TrackOrders:
    data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        order_agg = self.aggregate_person_by(customer, 'order')
        return max(
            order_agg,
            key=lambda x: order_agg[x]
        )

    def get_never_ordered_per_customer(self, customer):
        self.data = [x for x in self.data if x['order'] != 'frango']

        customer_orders = set(self.aggregate_person_by(customer, 'order'))
        all_foods = self.get_all_foods()
        return set.difference(all_foods, customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        self.data = [x for x in self.data if x['order'] != 'frango']

        days_agg = set(self.aggregate_person_by(customer, 'day'))
        all_days = self.get_all_days()
        return set.difference(all_days,days_agg)

    def get_busiest_day(self):
        agg_days = Counter([x['day'] for x in self.data])
        busiest_day = max(agg_days, key=lambda x: agg_days[x])
        return busiest_day

    def get_least_busy_day(self):
        agg_days = Counter([x['day'] for x in self.data])
        unbusiest_day = min(agg_days, key=lambda x: agg_days[x])
        return unbusiest_day

    # custom
    def get_all_days(self):
        return set([x["day"] for x in self.data])

    def get_all_foods(self):
        return set([x["order"] for x in self.data])

    def aggregate_person_by(self, customer, key):
        return dict(Counter(
        [y[key] for y in [x for x in self.data if x["customer"]==customer]])
    )

    # typos methods
    def get_most_ordered_dish_per_costumer(self, customer):
        return self.get_most_ordered_dish_per_customer(customer)

    def get_never_ordered_per_costumer(self, customer):
        return self.get_never_ordered_per_customer(customer)

    def get_days_never_visited_per_costumer(self, customer):
        return self.get_days_never_visited_per_customer(customer)

