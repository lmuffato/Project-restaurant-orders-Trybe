from src.analyze_log import orders_by_customer, most_requested
from src.analyze_log import find_foods_customer_never_buy
from src.analyze_log import find_days_customer_never_go
from src.analyze_log import busiest_day
from src.analyze_log import less_busy_day


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = orders_by_customer(self.orders, costumer)
        return most_requested(orders)

    def get_never_ordered_per_costumer(self, costumer):
        orders = orders_by_customer(self.orders, costumer)
        output = find_foods_customer_never_buy(self.orders, orders)
        return output

    def get_days_never_visited_per_costumer(self, costumer):
        orders = orders_by_customer(self.orders, costumer)
        output = find_days_customer_never_go(self.orders, orders)
        return output

    def get_busiest_day(self):
        return busiest_day(self.orders)

    def get_least_busy_day(self):
        return less_busy_day(self.orders)
