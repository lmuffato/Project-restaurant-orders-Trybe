class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_count = []
        for order in self.orders:
            if order[0] == costumer:
                order_count.append(order[1])
        return max(set(order_count), key=order_count.count)

    def get_never_ordered_per_costumer(self, costumer):
        available_meals = []
        for order in self.orders:
            if order[1] not in available_meals:
                available_meals.append(order[1])
        orders = []
        for order in self.orders:
            if order[0] == costumer and order[1] not in orders:
                orders.append(order[1])
        return set(available_meals).difference(set(orders))

    def get_days_never_visited_per_costumer(self, costumer):
        available_days = []
        for order in self.orders:
            if order[2] not in available_days:
                available_days.append(order[2])
        days_gone = []
        for order in self.orders:
            if order[0] == costumer and order[2] not in days_gone:
                days_gone.append(order[2])
        return set(available_days).difference(set(days_gone))

    def get_busiest_day(self):
        days_count = []
        for order in self.orders:
            days_count.append(order[2])
        return max(set(days_count), key=days_count.count)

    def get_least_busy_day(self):
        days_count = []
        for order in self.orders:
            days_count.append(order[2])
        return min(set(days_count), key=days_count.count)
