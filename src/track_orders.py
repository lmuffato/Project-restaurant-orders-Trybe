class TrackOrders:
    orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_orders_by_name(self):
        all_orders = {}
        for name, order, week_day in self.orders:
            if name not in all_orders:
                all_orders[name] = []
            all_orders[name].append((order, week_day))
        return all_orders

    def get_most_ordered_dish_per_costumer(self, costumer):
        all_orders = self.get_orders_by_name()
        person_orders = all_orders[costumer]

        count = {}
        most_ordered = person_orders[0][0]

        for order, day in person_orders:
            if order not in count:
                count[order] = 1
            else:
                count[order] += 1

            if count[order] > count[most_ordered]:
                most_ordered = order

        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
