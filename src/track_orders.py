class TrackOrders:
    def __init__(self):
        self.qtd_orders = 0
        self.orders = []

    def __len__(self):
        return self.qtd_orders

    def get_data_per_name(self, costomer):
        return [
            order for order in self.orders if order['costumer'] == costomer
        ]

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})
        self.qtd_orders += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        person_orders = self.get_data_per_name(costumer)
        most_ordered = self.orders[0]['order']
        count = {}

        for order in person_orders:
            if order['order'] not in count:
                count[order['order']] = 1
            else:
                count[order['order']] += 1

            if count[order['order']] > count[most_ordered]:
                most_ordered = order['order']

        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        person_orders = self.get_data_per_name(costumer)
        all_orders = set([order['order'] for order in self.orders])
        person_orders_unique = set([order['order'] for order in person_orders])

        return all_orders.difference(person_orders_unique)

    def get_days_never_visited_per_costumer(self, costumer):
        person_orders = self.get_data_per_name(costumer)
        days = set([order['day'] for order in self.orders])
        person_days = set([order['day'] for order in person_orders])

        return days.difference(person_days)

    def get_busiest_day(self):
        day = self.orders[0]['day']
        count = {}

        for order in self.orders:
            if order['day'] not in count:
                count[order['day']] = 1
            else:
                count[order['day']] += 1
        return day

    def get_least_busy_day(self):
        day = self.orders[0]['day']
        count = {}
        for order in self.orders:
            if order['day'] not in count:
                count[order['day']] = 1
            else:
                count[order['day']] += 1

            if count[order['day']] < count[day]:
                day = order['day']
        return day
