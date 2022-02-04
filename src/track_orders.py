from .analyze_log import maria_fav_food


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        create_order = {
            "name": costumer,
            "food": order,
            "day": day
        }
        self.orders.append(create_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return maria_fav_food(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
