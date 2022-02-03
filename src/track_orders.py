from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_list = self.orders
        costumer_orders = []
        for i in range(len(order_list)):
            if order_list[i][0] == costumer:
                costumer_orders.append(order_list[i][1])
        return list(Counter(costumer_orders))[1]

    def get_never_ordered_per_costumer(self, costumer):
        order_list = self.orders
        costumer_orders = set()
        all_orders = set()
        for i in range(len(order_list)):
            all_orders.add(order_list[i][1])
            if order_list[i][0] == costumer:
                costumer_orders.add(order_list[i][1])
        return all_orders.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        order_list = self.orders
        days_costumer_went = set()
        full_days = set()
        for i in range(len(order_list)):
            full_days.add(order_list[i][2])
            if order_list[i][0] == costumer:
                days_costumer_went.add(order_list[i][2])
        return full_days.difference(days_costumer_went)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
