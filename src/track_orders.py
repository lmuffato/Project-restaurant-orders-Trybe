from collections import Counter


# INFORMAÇÕES IMPORTANTES: dados[index][0] == "nome"
# dados[index][1] == "comida" / dados[index][2] == "dia"

class TrackOrders:
    # __init__ é o método construtor => Course 33:01
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        lista_de_pedidos = self.pedidos
        pedidos_do_cliente = []
        for index in range(len(lista_de_pedidos)):
            if lista_de_pedidos[index][0] == costumer:
                pedidos_do_cliente.append(lista_de_pedidos[index][1])
        return list(Counter(pedidos_do_cliente))[1]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
