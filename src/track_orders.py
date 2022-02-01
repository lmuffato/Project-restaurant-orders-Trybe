from statistics import mode
from collections import Counter
import src.analyze_log as analize


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analize.most_eaten_food(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return analize.costumer_never_interacted(self.orders, costumer, 1)

    def get_days_never_visited_per_costumer(self, costumer):
        return analize.costumer_never_interacted(self.orders, costumer, 2)

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return mode(days)

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        frequent = Counter(days).most_common()
        return frequent[-1][0]
