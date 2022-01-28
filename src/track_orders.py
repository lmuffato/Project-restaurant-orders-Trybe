class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        logs_costumer = [
            log for log in self.orders if log[0] == costumer
            ]

        favorite_dish_costumer = self.orders[0][1]
        dishs_costumer = {}

        for log in logs_costumer:
            if log[1] in dishs_costumer:
                dishs_costumer[log[1]] += 1
            else:
                dishs_costumer[log[1]] = 0

            if dishs_costumer[log[1]] > dishs_costumer[favorite_dish_costumer]:
                favorite_dish_costumer = log[1]

        return favorite_dish_costumer

    def get_never_ordered_per_costumer(self, costumer):
        food_costumer = set()
        all_food = set()

        for log in self.orders:
            all_food.add(log[1])
            if log[0] == costumer:
                food_costumer.add(log[1])

        return all_food - food_costumer

    def get_days_never_visited_per_costumer(self, costumer):
        days_costumer = set()
        all_days = set()

        for log in self.orders:
            all_days.add(log[1])
            if log[0] == costumer:
                days_costumer.add(log[1])

        return all_days - days_costumer

    def get_busiest_day(self):
        busiest_day = self.orders[0][1]
        all_days = {}

        for log in self.orders:
            if log[1] in all_days:
                all_days[log[1]] += 1
            else:
                all_days[log[1]] = 0

            if all_days[log[1]] > all_days[busiest_day]:
                busiest_day = log[1]

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = self.orders[0][1]
        all_days = {}

        for log in self.orders:
            if log[1] in all_days:
                all_days[log[1]] += 1
            else:
                all_days[log[1]] = 0

            if all_days[log[1]] < all_days[least_busy_day]:
                least_busy_day = log[1]

        return least_busy_day
