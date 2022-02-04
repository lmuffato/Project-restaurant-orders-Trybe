class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_frequent = self.orders
        for food in self.orders:
            if food == costumer:
                if food not in count:
                    count[food] = 1
                else:
                    count[food] += 1

                if count[food] > count[most_frequent]:
                    most_frequent = food

        return most_frequent[1][1]

    def get_never_ordered_per_costumer(self, costumer):
        aux_all_customers = []
        aux_customer = []
        for food in self.orders:
            aux_all_customers.append(food[1])
            if food[0] == costumer:
                aux_customer.append(food[1])

        make_intersection = set(aux_all_customers).difference(
            set(aux_customer)
        )

        return make_intersection

    def get_days_never_visited_per_costumer(self, costumer):
        aux_all_customers = []
        aux_customers = []
        for food in self.orders:
            aux_all_customers.append(food[2])
            if food[0] == costumer:
                aux_customers.append(food[2])

        make_intersection = set(aux_all_customers).difference(
            set(aux_customers)
        )

        return make_intersection

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
