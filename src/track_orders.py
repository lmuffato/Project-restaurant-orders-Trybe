class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        pass

    def get_most_ordered_dish_per_costumer(self, customer):
        pass

    def get_never_ordered_per_costumer(self, customer):
        pass

    def get_days_never_visited_per_costumer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
