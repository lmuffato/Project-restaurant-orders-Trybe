class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_by_costumer = []

        for order in self.orders:
            if (
                order["costumer"] == costumer
                and order["order"] not in order_by_costumer
            ):
                order_by_costumer[order["order"]] = 1
            elif order["costumer"] == costumer:
                order_by_costumer[order["order"]] += 1

        return max(order_by_costumer, key=order_by_costumer.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        all_meals = set()
        ordered_by_costumer = set()

        for order in self.orders:
            if order["costumer"] == costumer:
                ordered_by_costumer.add(order["order"])
            all_meals.add(order["order"])

        return all_meals.difference(ordered_by_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_visited = set()

        for order in self.orders:
            if order["costumer"] == costumer:
                days_visited.add(order["day"])
            days.add(order["day"])

        return days.difference(days_visited)

    def get_busiest_day(self):
        days = {}

        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order["day"]] += 1

        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}

        for order in self.orders:
            if order["day"] not in days:
                days[order["day"]] = 1
            else:
                days[order["day"]] += 1

        return min(days, key=days.get)
