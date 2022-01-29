class TrackOrders:
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add_new_order(self, costumer, order, day):
        self.order.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = []
        for order in self.order:
            if order[0] == costumer:
                costumer_orders.append(order[1])
        most_ordered = costumer_orders[0]
        count = {}
        for order in costumer_orders:
            if order not in count:
                count[order] = 1
            else:
                count[order] += 1

            if count[order] > count[most_ordered]:
                most_ordered = order
        return most_ordered


    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
