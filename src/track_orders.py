from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_list = self.orders
        costumers_orders = []
        for index in range(len(orders_list)):
            if orders_list[index][0] == costumer:
                costumers_orders.append(orders_list[index][1])
        return list(Counter(costumers_orders))[1]

    def get_never_ordered_per_costumer(self, costumer):
        orders_list = self.orders
        costumers_orders = set()
        all_dishes = set()
        for index in range(len(orders_list)):
            all_dishes.add(orders_list[index][1])
            if orders_list[index][0] == costumer:
                costumers_orders.add(orders_list[index][1])
        return all_dishes.difference(costumers_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        orders_list = self.orders
        costumers_days = set()
        all_days = set()
        for index in range(len(orders_list)):
            all_days.add(orders_list[index][2])
            if orders_list[index][0] == costumer:
                costumers_days.add(orders_list[index][2])
        return all_days.difference(costumers_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
