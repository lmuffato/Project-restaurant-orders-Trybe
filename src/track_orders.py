class TrackOrders:
    # ref do init, course / curso na alura / youtube
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)  # convoca o init e retorna o tamanho

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        # cria um novo pedido, com client/pedido/dia

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
