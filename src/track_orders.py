class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        dishes = {}
        for order in self.orders:
            person, dish, _day = order
            if person == costumer:
                if dish not in dishes:
                    dishes[dish] = 1
                else:
                    dishes[dish] += 1
        max_value = max(dishes.values())
        result = [key for key, value in dishes.items() if value == max_value]
        return result[0]

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set()
        customer_dishes = set()
        for order in self.orders:
            person, dish, _day = order
            if dish not in dishes:
                dishes.add(dish)
            if person == costumer and dish not in customer_dishes:
                customer_dishes.add(dish)
        result = customer_dishes.symmetric_difference(dishes)
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        weekdays = set()
        customer_checkin_day = set()

        for order in self.orders:
            person, _dish, day = order
            if day not in weekdays:
                weekdays.add(day)
            if person == costumer and day not in customer_checkin_day:
                customer_checkin_day.add(day)

        result = customer_checkin_day.symmetric_difference(weekdays)
        return result

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
