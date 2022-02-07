from collections import Counter


class TrackOrders:
    def __init__(self):
        self.lista_pedidos = []

    def __len__(self):
        return len(self.lista_pedidos)

    def add_new_order(self, costumer, order, day):
        self.lista_pedidos.append({
            'customer': costumer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals_list = []
        for row in self.lista_pedidos:
            if row['customer'] == costumer:
                meals_list.append(row['order'])
        c = Counter(meals_list)
        a_mais_pedida = c.most_common(1)[0][0]
        return a_mais_pedida

    def get_never_ordered_per_costumer(self, costumer):
        meals_list = []
        all_meals = []
        for row in self.lista_pedidos:
            all_meals.append(row['order'])
            if row['customer'] == costumer:
                meals_list.append(row['order'])

        e = set(all_meals)
        c = set(meals_list)
        return e.difference(c)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = []
        que_day = []
        for row in self.lista_pedidos:
            all_days.append(row['day'])
            if row['customer'] == costumer:
                que_day.append(row['day'])

        a = set(all_days)
        b = set(que_day)
        return a.difference(b)

    def get_busiest_day(self):
        busy_day = []
        for row in self.lista_pedidos:
            busy_day.append(row['day'])
        b = Counter(busy_day)
        a = b.most_common(1)[0][0]
        return a

    def get_least_busy_day(self):
        not_busy = []
        for row in self.lista_pedidos:
            not_busy.append(row['day'])
        z = Counter(not_busy)
        y = z.most_common()
        return y[-1][0]  # ultimo da lista, primeiro da tupla
