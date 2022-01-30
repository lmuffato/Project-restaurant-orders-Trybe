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
        lista_de_pedidos = self.pedidos
        todos_os_pratos = set()
        pratos_do_cliente = set()
        for index in range(len(lista_de_pedidos)):
            todos_os_pratos.add(lista_de_pedidos[index][1])
            if lista_de_pedidos[index][0] == costumer:
                pratos_do_cliente.add(lista_de_pedidos[index][1])
        return todos_os_pratos.difference(pratos_do_cliente)

    def get_days_never_visited_per_costumer(self, costumer):
        lista_de_pedidos = self.pedidos
        todos_os_dias = set()
        dias_do_cliente = set()
        for index in range(len(lista_de_pedidos)):
            todos_os_dias.add(lista_de_pedidos[index][2])
            if lista_de_pedidos[index][0] == costumer:
                dias_do_cliente.add(lista_de_pedidos[index][2])
        return todos_os_dias.difference(dias_do_cliente)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
