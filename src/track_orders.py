from collections import Counter


class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_ordered_dish = []
        for order in self.orders:
            if order[0] == costumer:
                most_ordered_dish.append(order[1])
        return Counter(most_ordered_dish).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        week_days = []
        for order in self.orders:
            week_days.append(order[2])
        return Counter(week_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        week_days = []
        for order in self.orders:
            week_days.append(order[2])
        return Counter(week_days).most_common()[-1][0]
