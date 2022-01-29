class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return self.orders

    def add_new_order(self, costumer, order, day):
        return self.orders.append({
            "name": costumer,
            "food": order,
            "week": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        most_frequent_food = self.orders[0]["food"]
        frequency = {}

        for order in self.orders:
            if order["name"] == costumer:
                if order["food"] not in frequency:
                    frequency[order["food"]] = 1
                else:
                    frequency[order["food"]] += 1
                if frequency[order["food"]] > frequency[most_frequent_food]:
                    most_frequent_food = order["food"]

        return most_frequent_food

    def get_never_ordered_per_costumer(self, costumer):
        list = []
        list_not_order_food = []
        for order in self.orders:
            if order["name"] == costumer and order["food"] not in list:
                list.append(order["food"])

        for order in self.orders:
            if (
                order["food"] not in list
                and order["food"] not in list_not_order_food
            ):
                list_not_order_food.append(order["food"])
        return set(list_not_order_food)

    def get_days_never_visited_per_costumer(self, costumer):
        list = []
        list_day_never_went = []
        for order in self.orders:
            if order["name"] == costumer and order["week"] not in list:
                list.append(order["week"])

        for order in self.orders:
            if (
                order["week"] not in list
                and order["week"] not in list_day_never_went
            ):
                list_day_never_went.append(order["week"])
        return set(list_day_never_went)

    def get_busiest_day(self):
        busiest_day = self.orders[0]["week"]
        frequency = {}

        for order in self.orders:
            if order["week"] not in frequency:
                frequency[order["week"]] = 1
            else:
                frequency[order["week"]] += 1
            if frequency[order["week"]] > frequency[busiest_day]:
                busiest_day = order["week"]

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = self.orders[0]["week"]
        frequency = {}

        for order in self.orders:
            if order["week"] not in frequency:
                frequency[order["week"]] = 1
            else:
                frequency[order["week"]] += 1
            if frequency[order["week"]] < frequency[least_busy_day]:
                least_busy_day = order["week"]

        return least_busy_day
