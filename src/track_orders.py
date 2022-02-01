class TrackOrders:
    def __init__(self):
        self.orders = []
        self.costumers = set()
        self.meals = set()
        self.days = set()
        self.costumer_orders = {}

    def __len__(self):
        return len(self.orders)

    def data_parser(self, costumer, meal, day):
        if costumer not in self.costumers:
            self.costumers.add(costumer)
        if meal not in self.meals:
            self.meals.add(meal)
        if day not in self.days:
            self.days.add(day)

        if costumer not in self.costumer_orders:
            self.costumer_orders[costumer] = [(meal, day)]
        else:
            self.costumer_orders[costumer].append((meal, day))

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))
        self.data_parser(costumer, order, day)

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_days = set()
        for _meal, day in self.costumer_orders[costumer]:
            if day not in costumer_days:
                costumer_days.add(day)
        return self.days.difference(costumer_days)

    def get_busiest_day(self):
        counter = {}
        bigger = 0
        busiest = ""
        for _costumer, _meal, day in self.orders:
            if day not in counter:
                counter[day] = 1
            else:
                counter[day] += 1
            if counter[day] > bigger:
                bigger = counter[day]
                busiest = day
        return busiest

    def get_least_busy_day(self):
        counter = {}
        for _costumer, _meal, day in self.orders:
            if day not in counter:
                counter[day] = 1
            else:
                counter[day] += 1

        smallest = False
        not_busy = ""
        for day, count in counter.items():
            if not smallest or count < smallest:
                smallest = count
                not_busy = day
        return not_busy
