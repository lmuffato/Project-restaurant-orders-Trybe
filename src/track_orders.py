class TrackOrders:
    def __len__(self):
        pass

    def add_new_order(self, costumer, order, day):
        if costumer in self.orders:
            self.orders[costumer].append((order, day))
        else:
            self.orders[costumer] = [(order, day)]
        self.menu.add(order)
        self.days.append(day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
