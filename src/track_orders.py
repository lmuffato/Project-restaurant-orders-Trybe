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
        customer_orders = []
        recipes = []

        for i in self.orders:
            recipes.append(i[1])
            if i[0] == costumer:
                customer_orders.append(i[1])
        return set(recipes).symmetric_difference(set(customer_orders))


    def get_days_never_visited_per_costumer(self, costumer):
        customer_orders = []
        days = []

        for i in self.orders:
            days.append(i[2])
            if i[0] == costumer:
                customer_orders.append(i[2])
        return set(days).symmetric_difference(set(customer_orders))


    def get_busiest_day(self):
        days = list()

        for data in self.orders:
            days.append(data[2])

        return max(set(days), key=days.count)


    def get_least_busy_day(self):
        days = list()

        for data in self.orders:
            days.append(data[2])

        return min(set(days), key=days.count)
