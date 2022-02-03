from collections import Counter


# agradeço aos colegas Carlos sá, e murilo gonçalvez
# pela ajuda no entendimento do projeto

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
        orders_list = self.orders
        client_orders = list()
        for i in range(len(orders_list)):
            if orders_list[i][0] == costumer:
                client_orders.append(orders_list[i][1])
        counter = Counter(client_orders)
        return list(counter)[1]
        # parecido com a da maria porem "o método retorna o prato mais pedido."

    def get_never_ordered_per_costumer(self, costumer):
        orders_list = self.orders
        all_dishes = set()
        dishes_client = set()
        for i in range(len(orders_list)):
            all_dishes.add(orders_list[i][1])
            if orders_list[i][0] == costumer:
                dishes_client.add(orders_list[i][1])
        return all_dishes.difference(dishes_client)

    def get_days_never_visited_per_costumer(self, costumer):
        orders_list = self.orders
        all_days = set()
        client_day = set()
        for i in range(len(orders_list)):
            all_days.add(orders_list[i][2])
            if orders_list[i][0] == costumer:
                client_day.add(orders_list[i][2])
        return all_days.difference(client_day)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
