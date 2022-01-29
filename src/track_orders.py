import src.analyze_log as analyze_log


class TrackOrders:
    def __init__(self):
        self.requests = []

    def __len__(self):
        return len(self.requests)

    # Registra um pedido
    def add_new_order(self, costumer, order, day):
        self.requests.append([costumer, order, day])

    # Retorna o prato mais pedido
    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyze_log.most_request_dish(self.requests, costumer)

    # Retorna o prato que a pessao nunca pediu
    def get_never_ordered_per_costumer(self, costumer):

        pass

    # Retorna o dia que a pessoa nunca foi ao restaurante
    def get_days_never_visited_per_costumer(self, costumer):

        pass

    # Retorna o dia mais movimentado
    def get_busiest_day(self):
        days_of_week = [requests[2] for requests in self.requests]
        return max(set(days_of_week), key=days_of_week.count)

    # Retorna o da menos moviimentado
    def get_least_busy_day(self):
        days_of_week = [requests[2] for requests in self.requests]
        return min(set(days_of_week), key=days_of_week.count)
