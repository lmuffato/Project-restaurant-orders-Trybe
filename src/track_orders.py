from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        new_order = {'customer': customer, "order": order, "day": day}

        self.orders.append(new_order)

    def get_orders_per_costumer(self, customer):
        filtered_data = [
          item for item in self.orders if item["customer"] == customer
          ]

        return filtered_data

    def get_most_ordered_dish_per_costumer(self, customer):
        filtered_order = self.get_orders_per_costumer(customer)

        filtered_data = [item["order"] for item in filtered_order]
        count_order = Counter(filtered_data)

        return count_order.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, customer):
        filtered_order = self.get_orders_per_costumer(customer)

        general_order = set([item["order"] for item in self.orders])
        customer_order = set([item["order"] for item in filtered_order])

        return general_order.difference(customer_order)

    def get_days_never_visited_per_costumer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
