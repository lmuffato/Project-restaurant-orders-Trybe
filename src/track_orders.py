import collections


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"costumer": costumer, "order": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for item in self.orders:
            if item["costumer"] == costumer:
                orders.append(item["order"])
        return collections.Counter(orders).most_common(1)[0][0]
        # https://www.kite.com/python/docs/collections.Counter.most_common

    def get_never_ordered_per_costumer(self, costumer):
        for item in self.orders:
            if item["costumer"] == costumer:
                ordered_foods = set(item["order"])
                never_ordered_foods = set(item["order"])
        return never_ordered_foods.difference(ordered_foods)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
