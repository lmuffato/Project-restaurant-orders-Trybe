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
        days_costumer_go = set()
        days = set()

        for order in self._orders:
            person, _dish, day = order
            if day not in days:
                days.add(day)
            if person == costumer and day not in days_costumer_go:
                days_costumer_go.add(day)

        return days_costumer_go.symmetric_difference(days)

    def get_busiest_day(self):
        costumers_quantity_per_day = {}
        for order in self._orders:
            _person, _dish, day = order
            if day not in costumers_quantity_per_day:
                costumers_quantity_per_day[day] = 1
            else:
                costumers_quantity_per_day[day] += 1
        max_value = max(costumers_quantity_per_day.values())
        max_key = [
            key
            for key, value in costumers_quantity_per_day.items()
            if value == max_value
        ]
        return max_key[0]

    def get_least_busy_day(self):
        costumers_quantity_per_day = {}
        for order in self._orders:
            _person, _dish, day = order
            if day not in costumers_quantity_per_day:
                costumers_quantity_per_day[day] = 1
            else:
                costumers_quantity_per_day[day] += 1
        min_value = min(costumers_quantity_per_day.values())
        min_key = [
            key
            for key, value in costumers_quantity_per_day.items()
            if value == min_value
        ]
        return min_key[0]
