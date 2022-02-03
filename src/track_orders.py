class TrackOrders:
    orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = [
            costumer_order["order"]
            for costumer_order in self.orders
            if costumer_order["costumer"] == costumer
        ]

        return max(customer_orders, key=customer_orders.count)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
