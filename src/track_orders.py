

class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        personsOrders = list()
        for personName, order, date in self.orders:
            if personName == costumer:
                personsOrders.append(order)
        return max(personsOrders, key=personsOrders.count)

    def get_never_ordered_per_costumer(self, costumer):
        personsOrders = set()
        menu = set()
        neverOrdered = set()
        for personName, personOrder, date in self.orders:
            if personName == costumer:
                personsOrders.add(personOrder)
            menu.add(personOrder)
        for ordered in menu:
            if ordered not in personsOrders:
                neverOrdered.add(ordered)
        return neverOrdered

    def get_days_never_visited_per_costumer(self, costumer):
        frequented_days = set()
        schedule = set()
        not_frequented = set()
        for personName, personOrder, date in self.orders:
            if personName == costumer:
                frequented_days.add(date)
            schedule.add(date)
        for day in schedule:
            if day not in frequented_days:
                not_frequented.add(day)
        return not_frequented

    def get_busiest_day(self):
        frequentedDays = list()
        for personName, order, date in self.orders:
            frequentedDays.append(date)
        return max(frequentedDays, key=frequentedDays.count)

    def get_least_busy_day(self):
        frequentedDays = list()
        for personName, order, date in self.orders:
            frequentedDays.append(date)
        return min(frequentedDays, key=frequentedDays.count)
