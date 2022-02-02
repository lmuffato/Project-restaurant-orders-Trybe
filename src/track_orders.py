class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def count_elements(data):
        result = {order: data.count(order) for order in set(data)}
        return result

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = []
        for row in costumer:
            result.append(row["order"])
        result = self.count_elements(result)
        result = max(result, key=result.get)
        return result

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
