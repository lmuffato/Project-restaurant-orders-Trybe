from collections import Counter

# https://app.betrybe.com/course/computer-science/programacao-orientada-a-objetos-e-padroes-de-projeto/
# heranca-composicao-e-interfaces/7c4613cf-5e5d-4a3f-8551-c891a2dee6d5/
# o-que-vamos-aprender/7282d877-759f-4899-925c-53883983a3f0?use_case=calendar


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_list = self.orders
        client_orders = []
        for index in range(len(orders_list)):
            if orders_list[index][0] == costumer:
                client_orders.append(orders_list[index][1])
        total_orders = list(Counter(client_orders))[1]
        return total_orders

    def get_never_ordered_per_costumer(self, costumer):
        orders_list = self.orders
        all_dishes = set()
        clients_dishes = set()
        for index in range(len(orders_list)):
            all_dishes.add(orders_list[index][1])
            if orders_list[index][0] == costumer:
                clients_dishes.add(orders_list[index][1])
        never_ordered_dishes = all_dishes.difference(clients_dishes)
        return never_ordered_dishes

    def get_days_never_visited_per_costumer(self, costumer):
        orders_list = self.orders
        every_day = set()
        clients_days = set()
        for index in range(len(orders_list)):
            every_day.add(orders_list[index][2])
            if orders_list[index][0] == costumer:
                clients_days.add(orders_list[index][2])
        empty_restaurant_days = every_day.difference(clients_days)
        return empty_restaurant_days

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
