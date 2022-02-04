class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_costumer = []
        for order in self.orders:
            if order["costumer"] == costumer:
                orders_by_costumer.append(order["order"])
        return max(set(orders_by_costumer), key=orders_by_costumer.count)

    def get_never_ordered_per_costumer(self, costumer):
        orders_by_costumer = []
        recipes = []
        for order in self.orders:
            recipes.append(order["order"])
            if order["costumer"] == costumer:
                orders_by_costumer.append(order["order"])
        return set(recipes).symmetric_difference(set(orders_by_costumer))

    def get_days_never_visited_per_costumer(self, costumer):
        days_visted = []
        days = []
        for order in self.orders:
            days.append(order["day"])
            if order["costumer"] == costumer:
                days_visted.append(order["day"])
        return set(days).symmetric_difference(set(days_visted))

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order["day"])
        return max(set(days), key=days.count)

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order["day"])
        return min(set(days), key=days.count)
