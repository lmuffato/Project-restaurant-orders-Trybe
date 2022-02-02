# import src.analyze_log as analyze_log
from src import analyze_log
from typing import Counter


class TrackOrders:
    def __init__(self):
        self.list_orders = []

    def __len__(self):
        return len(self.list_orders)

    def add_new_order(self, costumer, order, day):
        self.list_orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyze_log.food_most_ordered_by_costumer(
            costumer, self.list_orders)

    def get_never_ordered_per_costumer(self, costumer):
        return analyze_log.not_ordered_by_costumer(costumer, self.list_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        return analyze_log.not_attended_by_costumer(costumer, self.list_orders)

    def get_busiest_day(self):
        frequency_of_days = self.get_frequency_of_days()
        return Counter(frequency_of_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        frequency_of_days = self.get_frequency_of_days()
        return Counter(frequency_of_days).most_common(3)[2][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        return analyze_log.not_attended_by_costumer(
            costumer, order, self.list_orders)

    def get_frequency_of_days(self):
        frequency_of_days = []
        for order in self.list_orders:
            frequency_of_days.append(order[2])
        return frequency_of_days
