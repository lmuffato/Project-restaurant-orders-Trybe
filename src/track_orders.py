from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_data = [
            order[1] for order in self.orders if order[0] == costumer
        ]
        count = Counter(customer_data)
        most_ordered = count.most_common(1)[0][0]
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        return Counter([order[2] for order in self.orders]).most_common(1)[0][
            0
        ]

    def get_least_busy_day(self):
        return Counter([order[2] for order in self.orders]).most_common()[-1][
            0
        ]
