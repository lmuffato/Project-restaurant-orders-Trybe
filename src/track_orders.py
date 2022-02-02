class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"name": costumer, "food": order, "day": day}
        )

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_frequent_ordered = self.orders[0]["food"]
        frequency = {}

        for order in self.orders:
            if order["name"] == costumer:
                if order["food"] not in frequency:
                    frequency[order["food"]] = 1
                else:
                    frequency[order["food"]] += 1
                if frequency[order["food"]] > frequency[most_frequent_ordered]:
                    most_frequent_ordered = order["food"]

        return most_frequent_ordered

    def get_never_ordered_per_costumer(self, costumer):
        list_ordered = set()
        list_never_ordered = set()
        for order in self.orders:
            if order["name"] == costumer:
                list_ordered.add(order["food"])
            list_never_ordered.add(order["food"])
        return list_never_ordered.difference(list_ordered)

    """ https://app.betrybe.com/course/computer-science/estrutura-de-dados-i/set/
    e4286822-c7c1-44a8-9baf-089446774ccf/
    conteudo/1702f410-7728-4ad9-b3b8-8e3cdc4eb53b/resumao-resolucao-de-problemas/
    171e3e2d-770d-4c7f-97fc-f60f2f2cfaa6?use_case=side_bar """

    def get_days_never_visited_per_costumer(self, costumer):
        set_day_ordered = set()
        set_day_never = set()
        for order in self.orders:
            if order["name"] == costumer:
                set_day_ordered.add(order["day"])
            set_day_never.add(order["day"])
        return set_day_never.difference(set_day_ordered)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
