from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def get_orders(self):
        return self.orders

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = filter(
            lambda order: order["costumer"] == costumer, self.orders
        )
        orders = map(lambda order: order["order"], customer_orders)
        count_orders = Counter(orders)
        return count_orders.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set(map(lambda order: order["order"], self.orders))
        customer_orders = filter(
            lambda order: order["costumer"] == costumer, self.orders
        )
        never_ordered = all_orders.difference(
            set(map(lambda order: order["order"], customer_orders))
        )
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set(map(lambda order: order["day"], self.orders))
        customer_orders = filter(
            lambda order: order["costumer"] == costumer, self.orders
        )
        never_visited = all_days.difference(
            set(map(lambda order: order["day"], customer_orders))
        )
        return never_visited

    def get_busiest_day(self):
        return Counter(
            map(lambda order: order["day"], self.orders)
        ).most_common(1)[0][0]

    def get_least_busy_day(self):
        return Counter(
            map(lambda order: order["day"], self.orders)
        ).most_common()[-1][0]
