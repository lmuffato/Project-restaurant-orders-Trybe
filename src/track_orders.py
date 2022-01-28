import src.analyze_log as func


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return func.most_ordered_food_per_customer(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return func.never_ordered_food_per_customer(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return func.never_went_per_customer(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
