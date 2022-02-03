from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)


    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])


    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = [order[1] for order in self.orders if order[0] == costumer]
        # print(f'Client_order: {client_orders}')
        return(Counter(client_orders).most_common()[0][0])

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set([order[1] for order in self.orders])
        client_dishes = set([order[1] for order in self.orders if costumer == order[0]])
        return all_dishes - client_dishes

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set([order[2] for order in self.orders])
        client_days = set([order[2] for order in self.orders if costumer == order[0]])
        return all_days - client_days


    def get_busiest_day(self):
        all_days = [order[2] for order in self.orders]
        return(Counter(all_days).most_common()[0][0])

    def get_least_busy_day(self):
        all_days = [order[2] for order in self.orders]
        return(Counter(all_days).most_common(-1)[0][0])
