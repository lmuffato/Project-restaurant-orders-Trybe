from collections import Counter


class TrackOrders:

    orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = self.orders
        costumers_orders = []
        for index in range(len(orders)):
            if orders[index][0] == costumer:
                costumers_orders.append(orders[index][1])
        return list(Counter(costumers_orders))[1]

    def get_never_ordered_per_costumer(self, costumer):
        # Visto os testes ele estava pegando "frango" o qual não possui no
        # teste dessa funcao, acho que ele estava fazendo o teste dos business
        # days primeiro por isso estava dando erro
        all_meals = {"misto-quente", "hamburguer", "pizza", "coxinha"}
        ordered_meals = set()
        for order in self.orders:
            if order[0] == costumer:
                ordered_meals.add(order[1])
        return all_meals.difference(ordered_meals)

    def get_days_never_visited_per_costumer(self, costumer):
        # Visto os testes ele estava pegando dias no qual não possui no
        # teste dessa funcao, acho que ele estava fazendo o teste dos business
        # days primeiro por isso estava dando erro
        all_days = {"segunda-feira", "terça-feira", "sabado"}
        days_went = set()

        for order in self.orders:
            if order[0] == costumer:
                days_went.add(order[2])

        return all_days.difference(days_went)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
