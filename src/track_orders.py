class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'cliente': costumer,
            'pedido': order,
            'dia': day,
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        order_count = {}
        most_frequent = self.orders[0]['pedido']

        for order in self.orders:
            pedido = order['pedido']
            if order['cliente'] == costumer:
                if pedido not in order_count:
                    order_count[pedido] = 1
                else:
                    order_count[pedido] += 1
                if (order_count[pedido] > order_count[most_frequent]):
                    most_frequent = pedido
        return most_frequent

    def get_never_ordered_per_costumer(self, costumer):
        orders_set = set()
        client_set = set()

        for order in self.orders:
            if order['cliente'] == costumer:
                client_set.add(order['pedido'])
            orders_set.add(order['pedido'])
        return orders_set.difference(client_set)

    def get_days_never_visited_per_costumer(self, costumer):
        orders_set = set()
        client_set = set()

        for order in self.orders:
            if order['cliente'] == costumer:
                client_set.add(order['dia'])
            orders_set.add(order['dia'])
        return orders_set.difference(client_set)

    def get_busiest_day(self):
        order_count = {}
        most_frequent = self.orders[0]['dia']

        for order in self.orders:
            dia = order['dia']
            if dia not in order_count:
                order_count[dia] = 1
            else:
                order_count[dia] += 1
            if (order_count[dia] > order_count[most_frequent]):
                most_frequent = dia
        return most_frequent

    def get_least_busy_day(self):
        order_count = {}
        less_frequent = self.orders[0]['dia']

        for order in self.orders:
            dia = order['dia']
            if dia not in order_count:
                order_count[dia] = 1
            else:
                order_count[dia] += 1
            if (order_count[dia] < order_count[less_frequent]):
                less_frequent = dia
        return less_frequent
