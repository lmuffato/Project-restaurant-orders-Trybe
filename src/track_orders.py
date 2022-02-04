class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = list()
        for cliente in self.pedidos:
            if cliente[0] == costumer:
                data.append(cliente[1])
        return max(set(data), key=data.count)

    def get_never_ordered_per_costumer(self, costumer):
        cliente_pedido = []
        recipes = []
        for row in self.pedidos:
            recipes.append(row[1])
            if row[0] == costumer:
                cliente_pedido.append(row[1])
        return set(recipes).symmetric_difference(set(cliente_pedido))

    def get_days_never_visited_per_costumer(self, costumer):
        cliente_pedido = []
        dias = []
        for row in self.pedidos:
            dias.append(row[2])
            if row[0] == costumer:
                cliente_pedido.append(row[2])
        return set(dias).symmetric_difference(set(cliente_pedido))

    def get_busiest_day(self):
        dias = list()
        for data in self.pedidos:
            dias.append(data[2])

        return max(set(dias), key=dias.count)

    def get_least_busy_day(self):
        dias = list()
        for data in self.pedidos:
            dias.append(data[2])

        return min(set(dias), key=dias.count)
