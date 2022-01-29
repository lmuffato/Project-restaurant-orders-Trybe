from .analyze_log import most_requested, filter_by_costumer
from .analyze_log import find_difference


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_data = filter_by_costumer(costumer, self.orders)
        return most_requested(costumer_data)

    def get_never_ordered_per_costumer(self, costumer):
        costumer_data = filter_by_costumer(costumer, self.orders)
        return find_difference(
            [product[1] for product in costumer_data],
            [product[1] for product in self.orders],
        )

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_data = filter_by_costumer(costumer, self.orders)
        return find_difference(
            [product[2] for product in costumer_data],
            [product[2] for product in self.orders],
        )

    def get_busiest_day(self):
        day_counter = {}
        busiest_day = self.orders[0][2]

        for item in self.orders:
            if item[2] in day_counter:
                day_counter[item[2]] += 1
            else:
                day_counter[item[2]] = 1

        if day_counter[item[2]] > day_counter[busiest_day]:
            busiest_day = item[2]

        return busiest_day

    def get_least_busy_day(self):
        pass
