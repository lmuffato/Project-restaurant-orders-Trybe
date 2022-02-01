class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "food": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_frequent_ordered = self.orders[0]["food"]
        frequency = {}

        for order in self.orders:
            if order["name"] == costumer:
                if order["food"] not in frequency:
                    frequency[order["food"]] = 1
                else:
                    frequency[order["food"]] += 1
                if frequency[order["food"]] > frequency[most_frequent_ordered]:
                    most_frequent_ordered = order["food"]

        return most_frequent_ordered

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
