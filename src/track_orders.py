from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_filtered_data_by_costumer(self, costumer):
        filtered_data = []

        for order in self.orders:
            if order["costumer"] == costumer:
                filtered_data.append(order)
        return filtered_data

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_data = self.get_filtered_data_by_costumer(costumer)

        total_eats = []
        for order in costumer_data:
            total_eats.append(order["order"])
        count = Counter(total_eats)

        return count.most_common(1)[0][0]

    def get_only_field(self, data, field):
        order_data = []

        for order in data:
            order_data.append(order[field])

        return order_data

    def get_never_ordered_per_costumer(self, costumer):
        costumer_data = self.get_filtered_data_by_costumer(costumer)

        all_orders = self.get_only_field(self.orders, "order")
        costumer_orders = self.get_only_field(costumer_data, "order")

        return set(all_orders) - set(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_data = self.get_filtered_data_by_costumer(costumer)

        all_orders = self.get_only_field(self.orders, "day")
        costumer_orders = self.get_only_field(costumer_data, "day")

        return set(all_orders) - set(costumer_orders)

    def get_busiest_day(self):
        all_orders = self.get_only_field(self.orders, "day")

        counter = Counter(all_orders)

        return counter.most_common(1)[0][0]

    def get_least_busy_day(self):
        all_orders = self.get_only_field(self.orders, "day")

        counter = Counter(all_orders)
        counter_length = len(counter)

        return counter.most_common(counter_length)[counter_length - 1][0]
