class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        new_order = {
            'costumer': costumer,
            'order': order,
            'day': day
        }
        self.orders.append(new_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_order = self.filter_by_client(costumer)
        count = {}
        most_ordered_dish = self.orders[0]['order']

        for item in client_order:
            if item['order'] not in count:
                count[item['order']] = 1
            else:
                count[item['order']] += 1

            if count[item['order']] > count[most_ordered_dish]:
                most_ordered_dish = item['order']

        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        client_order = self.filter_by_client(costumer)
        orders = set([order['order'] for order in self.orders])
        person_orders = set([order['order'] for order in client_order])

        return orders.difference(person_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        client_order = self.filter_by_client(costumer)
        days = set([order['day'] for order in self.orders])
        days_by_client = set([order['day'] for order in client_order])

        return days.difference(days_by_client)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def filter_by_client(self, costumer):
        return [
            order for order in self.orders if order['costumer'] == costumer
        ]
