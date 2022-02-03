class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        result = self.orders[0][2]
        busy_days = {}

        for item in self.orders:
            day = item[2]
            if day not in busy_days:
                busy_days[day] = 1
            else:
                busy_days[day] += 1
            if busy_days[result] < busy_days[day]:
                result = day
        return result

    def get_least_busy_day(self):
        result = self.orders[0][2]
        not_busy_days = {}

        for item in self.orders:
            day = item[2]
            if day not in not_busy_days:
                not_busy_days[day] = 1
            else:
                not_busy_days[day] += 1
            if not_busy_days[result] > not_busy_days[day]:
                result = day
        return result
