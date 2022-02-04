from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_data_per_costumer(self, costumer):
        return [item for item in self.orders if item["costumer"] == costumer]

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_data = self.get_data_per_costumer(costumer)

        return Counter(
            [order["order"] for order in costumer_data]
        ).most_common(1)[0][0]

    def get_field(self, data, field):
        return [order[field] for order in data]

    def get_never_ordered_per_costumer(self, costumer):
        costumer_data = self.get_data_per_costumer(costumer)

        orders_data = set(self.get_field(self.orders, "order"))
        orders_costomer = set(self.get_field(costumer_data, "order"))

        return orders_data.difference(orders_costomer)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_data = self.get_data_per_costumer(costumer)

        orders_data = set(self.get_field(self.orders, "day"))
        orders_costomer = set(self.get_field(costumer_data, "day"))

        return orders_data.difference(orders_costomer)

    def get_busiest_day(self):
        orders_data = self.get_field(self.orders, "day")

        counter = Counter(orders_data)

        return counter.most_common(1)[0][0]

    def get_least_busy_day(self):
        orders_data = self.get_field(self.orders, "day")

        counter = Counter(orders_data)
        counter_length = len(counter)

        return counter.most_common(counter_length)[counter_length - 1][0]
