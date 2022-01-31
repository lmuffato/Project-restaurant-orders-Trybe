import src.analyze_log as functions


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return functions.most_ordered_food_per_customer(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return functions.never_ordered_food_per_customer(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return functions.never_went_per_customer(self.orders, costumer)

    def get_busiest_day(self):
        days = {}
        for row in self.orders:
            if row[2] not in days:
                days[row[2]] = 1
            else:
                days[row[2]] += 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for row in self.orders_list:
            if row[2] not in days:
                days[row[2]] = 1
            else:
                days[row[2]] += 1
        return min(days, key=days.get)
