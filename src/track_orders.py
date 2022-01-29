class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):

        return self.orders.append({
            "nome": costumer,
            "comida": order,
            "semana": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        frequentEat = self.orders[0]['comida']
        frequency = {}

        for order in self.orders:
            if order['nome'] == costumer:
                if order['comida'] not in frequency:
                    frequency[order['comida']] = 1
                else:
                    frequency[order['comida']] += 1
                if frequency[order['comida']] > frequency[frequentEat]:
                    frequentEat = order['comida']
        return frequentEat

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
