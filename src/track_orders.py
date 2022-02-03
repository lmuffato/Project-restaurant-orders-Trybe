import collections


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"costumer_name": costumer, "order_food": order, "order_day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = []
        for item in self.orders:
            if item["costumer_name"] == costumer:
                orders.append(item["order_food"])
        # Fonte:
        # https://docs.python.org/dev/library/collections.html#counter-objects
        return collections.Counter(orders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        ordered_foods = set()
        no_ordered_foods = set()
        for item in self.orders:
            if item["costumer_name"] == costumer:
                ordered_foods.add(item["order_food"])
            no_ordered_foods.add(item["order_food"])
        return no_ordered_foods.difference(ordered_foods)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
