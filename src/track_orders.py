class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_unique_dishes(self):
        return set([order[1] for order in self.orders])

    def get_unique_days(self):
        return set([order[2] for order in self.orders])

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_count = {}
        for d in self.get_unique_dishes():
            dish_count[d] = self.get_dish_quantity_per_costumer(costumer, d)

        return max(dish_count, key=dish_count.get)

    def get_dish_quantity_per_costumer(self, costumer, order):
        dish_count = 0
        for o in self.orders:
            if (o[0] == costumer) and (o[1] == order):
                dish_count += 1

        return dish_count

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        unique_dishes = self.get_unique_dishes()
        not_ordered = unique_dishes

        for order in self.orders:
            if (order[0] == costumer) and order[1] in unique_dishes:
                not_ordered.remove(order[1])

        return not_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        unique_days = self.get_unique_days()
        not_visited = unique_days

        for order in self.orders:
            if (order[0] == costumer) and order[2] in unique_days:
                not_visited.remove(order[2])

        return not_visited

    def get_frequency(self):
        frequency = {}

        for order in self.orders:
            if order[2] in frequency.keys():
                frequency[order[2]] += 1
            else:
                frequency[order[2]] = 1

        return frequency

    def get_busiest_day(self):
        freq = self.get_frequency()
        return max(freq, key=freq.get)

    def get_least_busy_day(self):
        freq = self.get_frequency()
        return min(freq, key=freq.get)
