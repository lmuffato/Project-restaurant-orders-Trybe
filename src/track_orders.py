class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = list()

        for customer in self.orders:
            if customer[0] == costumer:
                data.append(customer[1])
        return max(set(data), key=data.count)

    def get_never_ordered_per_costumer(self, costumer):
        customer_orders = [row[1] for row in self.orders if row[0] == costumer]
        recipes = [row[1] for row in self.orders]

        return set(recipes) - set(customer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_orders_by_days = [
            row[2] for row in self.orders if row[0] == costumer
            ]
        days = [row[2] for row in self.orders]

        return set(days) - set(costumer_orders_by_days)

    def get_busiest_day(self):
        days = [data[2] for data in self.orders]
        return max(days, key=days.count)

    def get_least_busy_day(self):
        days = [data[2] for data in self.orders]
        return min(days, key=days.count)
