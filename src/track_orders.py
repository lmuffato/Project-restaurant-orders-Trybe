from collections import Counter
class TrackOrders:
    def __init__(self):
        self.orders = {}
        self.menu = set()
        self.days = []

    def __len__(self):
        length = 0
        for _, orders in self.orders.items():
            length += len(orders)
        return length

    def add_new_order(self, costumer, order, day):
        if costumer in self.orders:
            self.orders[costumer].append((order, day))
        else:
            self.orders[costumer] = [(order, day)]
        self.menu.add(order)
        self.days.append(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_by_customer = Counter(self.orders[costumer])
        most_ordered_by_customer = ordered_by_customer.most_common(1)[0][0][0]
        return most_ordered_by_customer

    def get_never_ordered_per_costumer(self, costumer):
        ordered_by_customer = set(order[0] for order in self.orders[costumer])
        never_ordered_by_customer = self.menu.difference(ordered_by_customer)
        return never_ordered_by_customer

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
