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
        client_orders = []
        for index in range(len(orders_list)):
            if orders_list[index][0] == costumer:
                client_orders.append(orders_list[index][1])
        total_orders = list(Counter(client_orders))[1]
        return total_orders

    def get_never_ordered_per_costumer(self, costumer):
        orders_list = self.orders
        all_dishes = set()
        clients_dishes = set()
        for index in range(len(orders_list)):
            all_dishes.add(orders_list[index][1])
            if orders_list[index][0] == costumer:
                clients_dishes.add(orders_list[index][1])
        never_ordered_dishes = all_dishes.difference(clients_dishes)
        return never_ordered_dishes


    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
