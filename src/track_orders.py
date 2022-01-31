class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        order = {
            'cliente': costumer,
            'pedido': order,
            'dia': day
        }
        self.orders.append(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_frequent = self.orders[0]['pedido']

        for item in self.orders:
            if item['cliente'] == costumer:
                if item['pedido'] not in count:
                    count[item['pedido']] = 1
                else:
                    count[item['pedido']] += 1

                if count[item['pedido']] > count[most_frequent]:
                    most_frequent = item['pedido']

        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        opt = set(row['pedido'] for row in self.orders)
        ordered = set()

        for item in self.orders:
            if item['cliente'] == costumer:
                ordered.add(item['pedido'])

        return opt.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
