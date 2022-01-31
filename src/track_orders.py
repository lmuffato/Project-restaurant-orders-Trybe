from src.vividict import Vividict


class TrackOrders:
    def __init__(self):
        self.orders = Vividict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        order_amount = self.parse_amount_to_int(
            self.get_orders_per_costumer(costumer)[order]
        )
        day_amount = self.parse_amount_to_int(
            self.get_days_per_costumer(costumer)[day]
        )

        self.orders[costumer]["orders"][order] = order_amount + 1
        self.orders[costumer]["days"][day] = day_amount + 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = list(self.get_orders_per_costumer(costumer).items())
        amount_per_order = [value[1] for value in orders]
        index_greater_order = amount_per_order.index(max(amount_per_order))

        return orders[index_greater_order][0]

    def get_never_ordered_per_costumer(self, costumer):
        possible_orders = self.get_possible_values_by_key("orders")
        costumer_orders = self.get_orders_per_costumer(costumer)

        return self.diff(possible_orders, costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        possible_days = self.get_possible_values_by_key("days")
        costumer_days = self.get_days_per_costumer(costumer)

        return self.diff(possible_days, costumer_days)

    def get_busiest_day(self):
        merged_orders = self.get_merged_orders()
        return max(merged_orders, key=merged_orders.get)

    def get_least_busy_day(self):
        merged_orders = self.get_merged_orders()
        return min(merged_orders, key=merged_orders.get)

    # utils
    def get_orders_per_costumer(self, costumer):
        return self.orders[costumer]["orders"]

    def get_days_per_costumer(self, costumer):
        return self.orders[costumer]["days"]

    def parse_amount_to_int(self, amount):
        return amount if type(amount) is int else 0

    def get_possible_values_by_key(self, key):
        possible_values = []

        for costumer in self.orders:
            possible_values = [*possible_values, *self.orders[costumer][key]]

        return list(set(possible_values))

    def diff(self, arr1, arr2):
        return set(arr1).difference(arr2)

    def get_merged_orders(self):
        orders = list(
            map(lambda order: order["days"], list(self.orders.values()))
        )

        orders_merged = Vividict()

        for order in orders:
            key, value = list(order.items())[0]
            orders_amount = self.parse_amount_to_int(orders_merged[key])
            orders_merged[key] = orders_amount + value

        return orders_merged
