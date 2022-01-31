from collections import Counter
from statistics import mode


class TrackOrders:
    available_foods = ['hamburguer', 'pizza', 'coxinha', 'misto-quente']
    openned_days = ['terça-feira', 'segunda-feira', 'sabado']

    def __init__(self):
        self.orders = {}
        self.orders_count = 0

    def __len__(self):
        return self.orders_count

    def add_new_order(self, costumer, order, day):
        self.orders_count += 1
        if costumer in self.orders:
            self.orders[costumer]['orders'].append(order)
            self.orders[costumer]['days_at_restaurant'].append(day)
        else:
            self.orders[costumer] = {
                'orders': [order],
                'days_at_restaurant': [day]}

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mode(self.orders[costumer]['orders'])

    def get_never_ordered_per_costumer(self, costumer):
        return set([food for food in self.available_foods
                if food not in self.orders[costumer]['orders']])

    def get_days_never_visited_per_costumer(self, costumer):
        return set([day for day in self.openned_days
                if day not in self.orders[costumer]['days_at_restaurant']])

    def concatenate_arrays(self):
        union_array = []
        for costumer in self.orders.keys():
            union_array += self.orders[costumer]['days_at_restaurant']
        return union_array

    def get_busiest_day(self):
        frequented_days_from_all_costumers = self.concatenate_arrays()
        return mode(frequented_days_from_all_costumers)

    def get_least_busy_day(self):
        frequented_days_from_all_costumers = self.concatenate_arrays()
        return Counter(frequented_days_from_all_costumers).most_common()[-1][0]
