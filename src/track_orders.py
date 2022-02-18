from collections import Counter


class TrackOrders:

    def __init__(self):  # construtor do python
        # Adicionar nova ordem de serviço
        self.lista_pedidos = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        # permite verificar o comprimento da classe diretamente
        # apos instanciar como track_orders = TrackOrders()
        # len(track_orders)

        return len(self.lista_pedidos)

    # ADICIONA UMA NOVA ORDEM DE PEDIDO
    def add_new_order(self, costumer, order, day):
        # adiciona o objeto abaixo ao array de pedidos
        self.lista_pedidos.append({
            'customer': costumer,
            'order': order,
            'day': day
        })
        return self.lista_pedidos

    # RETORNA A LISTA DE PEDIDOS
    def get_lista_pedidos(self):
        return self.lista_pedidos

    # RETORNA O PRATO MAIS PEDIDO PELO CLIENTE
    def get_most_ordered_dish_per_costumer(self, costumer):

        customer_list = []
        # pra cada pedido na lista de pedidos
        for pedidos in self.lista_pedidos:
            # se o valor da chave customer for igual a customer
            if pedidos['customer'] == costumer:
                # adiciona o pedido a lista pessoal do cliente
                customer_list.append(pedidos['order'])

        # Counter cria um objeto de chave e valor das contagens
        orders_statistics = Counter(customer_list)
        # most_comum() retorna um array ordenando os elementos
        # por chave e valor
        # exemplo: [('hamburguer', 3), ('pizza', 1), ('coxinha', 1)]
        a_mais_pedida = orders_statistics.most_common()
        # retorna o primeiro valor do primeiro elemento do array
        return a_mais_pedida[0][0]

    # RETORNA A COMIDA QUE O CLIENTE NUNCA PEDIU
    def get_never_ordered_per_costumer(self, costumer):
        customer_list = []  # pedidos do cliente
        all_orders = []  # todos os pedidos

        for pedidos in self.lista_pedidos:
            # cria um array apenas com os pedidos
            all_orders.append(pedidos['order'])

            # cria um array apenas com os pedidos do cliente
            if pedidos['customer'] == costumer:
                customer_list.append(pedidos['order'])

        # retorna os pedidos únicos (não duplicados)
        all_unique_orders = set(all_orders)
        # retorna os pedidos únicos do cliente
        customer_unique_orders = set(customer_list)
        # retorna os pedidos que existem em all_unique_orders e que
        # não existem em customer_unique_orders
        return all_unique_orders.difference(customer_unique_orders)

    # RETORNA O CONJUNTO DE DIAS QUE A PESSOA NUNCA COMEU
    def get_days_never_visited_per_costumer(self, costumer):
        customer_days = []
        all_days = []
        for pedidos in self.lista_pedidos:
            all_days.append(pedidos['day'])
            if pedidos['customer'] == costumer:
                customer_days.append(pedidos['day'])

        all_unique_days = set(all_days)
        customer_unique_days = set(customer_days)
        return all_unique_days.difference(customer_unique_days)

    # RETORNA UMA LISTA CONTENDO O DIA DE TODOS OS PEDIDOS
    def get_all_days_list(self):
        all_days = []
        for pedidos in self.lista_pedidos:
            all_days.append(pedidos['day'])
        return all_days

    # RETORNA O DIA DE QUE TEVE MAIS PEDIDOS
    def get_busiest_day(self):
        all_days = self.get_all_days_list()
        all_unique_days = Counter(all_days)
        days_statistics = all_unique_days.most_common()
        # primiero da lista
        return days_statistics[0][0]

    # RETORNA O DIA COM MENOS PEDIDOS
    def get_least_busy_day(self):
        all_days = self.get_all_days_list()
        all_unique_days = Counter(all_days)
        days_statistics = all_unique_days.most_common()
        # o [-1] é o ultimo da lista
        return days_statistics[-1][0]


# Teste automatizado
# python3 -m pytest tests/test_track_orders.py


# Teste manual
# csv_parsed = [
#     ["maria", "pizza", "terça-feira"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["joao", "hamburguer", "terça-feira"],
#     ["maria", "coxinha", "segunda-feira"],
#     ["arnaldo", "misto-quente", "terça-feira"],
#     ["jose", "hamburguer", "sabado"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["maria", "hamburguer", "terça-feira"],
#     ["joao", "hamburguer", "terça-feira"],
# ]

# instanciando o objeto
# track_orders = TrackOrders()

# carregando a classe
# for element in csv_parsed:
    # track_orders.add_new_order(element[0], element[1], element[2])

# print(track_orders.get_all_days_list())

# track_orders.get_busiest_day()
