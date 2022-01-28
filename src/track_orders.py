class TrackOrders:
    def __init__(self):
        self._orders = []

    def __len__(self):
        return len(self._orders)

    def add_new_order(self, costumer, order, day):
        self._orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes = {}
        for order in self._orders:
            person, dish, _day = order
            if person == costumer:
                if dish not in dishes:
                    dishes[dish] = 1
                else:
                    dishes[dish] += 1
        max_value = max(dishes.values())
        max_key = [key for key, value in dishes.items() if value == max_value]
        return max_key[0]

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        costumer_dishes = set()

        for order in self._orders:
            person, dish, _day = order
            if dish not in dishes:
                dishes.add(dish)
            if person == costumer and dish not in costumer_dishes:
                costumer_dishes.add(dish)

        return costumer_dishes.symmetric_difference(dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
