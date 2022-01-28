import src.analyze_log as analyze


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyze.most_requested_dish(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return analyze.never_requested_dishes(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return analyze.days_without_going(self.orders, costumer)

    def get_busiest_day(self):
        return analyze.busiest_day(self.orders)

    def get_least_busy_day(self):
        return analyze.least_busy_day(self.orders)
