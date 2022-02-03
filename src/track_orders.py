from src.analyze_log import mariaPedidos, contadorNegativo


class TrackOrders:
    def __init__(self) -> None:
        self.len = 0
        self.orders = []

    def __len__(self):
        return self.len

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.len += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return mariaPedidos(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return contadorNegativo(self.orders, 'plate', costumer)
   
    def get_days_never_visited_per_costumer(self, costumer):
        return contadorNegativo(self, 'day', costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
