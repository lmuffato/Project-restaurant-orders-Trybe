import src.analyze_log as analyze_log


class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyze_log.get_favorite_order(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return analyze_log.never_ordered_by_person(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return analyze_log.get_days_not_frequented_by_person(
            self.orders,
            costumer
        )

    def get_busiest_day(self):
        frequentedDays = list()
        for personName, order, date in self.orders:
            frequentedDays.append(date)
        return max(frequentedDays, key=frequentedDays.count)

    def get_least_busy_day(self):
        frequentedDays = list()
        for personName, order, date in self.orders:
            frequentedDays.append(date)
        return min(frequentedDays, key=frequentedDays.count)
