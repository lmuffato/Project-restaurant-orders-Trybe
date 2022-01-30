from collections import Counter


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        return self.orders.append({"a": costumer, "b": order, "c": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_by_client = []
        for item in self.orders:
            if item["a"] == costumer:
                order_by_client.append(item["b"])
        return Counter(order_by_client).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        dices_ordered = set()
        dices_never = set()
        for item in self.orders:
            if item["a"] == costumer:
                dices_ordered.add(item["b"])
            dices_never.add(item["b"])
        return dices_never.difference(dices_ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        day_ordered = set()
        day_never = set()
        for item in self.orders:
            if item["a"] == costumer:
                day_ordered.add(item["c"])
            day_never.add(item["c"])
        return day_never.difference(day_ordered)

    def get_busiest_day(self):
        day_busiest = []
        for item in self.orders:
            day_busiest.append(item["c"])
        return Counter(day_busiest).most_common(1)[0][0]

    def get_least_busy_day(self):
        day_least = []
        for item in self.orders:
            day_least.append(item["c"])

        return Counter(day_least).most_common()[-1][0]
