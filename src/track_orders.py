
class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):

        orders = [
            order["order"]
            for order in self.orders
            if order["costumer"] == costumer
        ]

        return max(orders, key=orders.count)

    def get_never_ordered_per_costumer(self, costumer):
        ordered = set()
        all_dishes = set()

        for item in self.orders:
            if item["costumer"] == costumer:
                ordered.add(item["order"])

            all_dishes.add(item["order"])

        return all_dishes.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        all_days = []

        for item in self.orders:
            all_days.append(item["day"])

        return max(set(all_days), key=all_days.count)

    def get_least_busy_day(self):
        pass
