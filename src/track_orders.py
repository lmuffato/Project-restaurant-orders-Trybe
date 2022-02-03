from .analyze_log import (
    get_requests,
    menu,
    get_days,
    days
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        order = (
            costumer,
            order,
            day,
        )

        self.orders.append(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        sorted_orders = get_requests(self.orders, costumer)
        most_ordered = max(sorted_orders, key=sorted_orders.get)

        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        sorted_orders = set(get_requests(self.orders, costumer))
        never_ordered = sorted_orders.symmetric_difference(menu)

        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        sorted_days = set(get_days(self.orders, costumer))
        days_off = sorted_days.symmetric_difference(days)

        return days_off

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
