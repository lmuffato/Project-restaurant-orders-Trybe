class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'order': order, 'costumer': costumer, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        filtered = list(
            filter(lambda o: o['costumer'] == costumer, self.orders))
        count_dict = {}
        for order in filtered:
            try:
                count_dict[order['order']] += 1
            except(KeyError):
                count_dict[order['order']] = 1
        return max(count_dict, key=count_dict.get)

    def get_never_ordered_per_costumer(self, costumer):
        print(self.orders)
        return_list = []
        ordered = list(
            filter(lambda o: o['costumer'] == costumer, self.orders))
        ordered = list(map(lambda o: o['order'], ordered))
        for order in self.orders:
            if order['costumer'] != costumer and order['order'] not in ordered:
                return_list.append(order['order'])
        return set(return_list)

    def get_days_never_visited_per_costumer(self, costumer):
        return_list = []
        ordered = list(
            filter(lambda o: o['costumer'] == costumer, self.orders))
        ordered = list(map(lambda o: o['day'], ordered))
        for order in self.orders:
            if order['costumer'] != costumer and order['day'] not in ordered:
                return_list.append(order['day'])
        return set(return_list)

    def get_busiest_day(self):
        count_dict = {}
        for order in self.orders:
            try:
                count_dict[order['day']] += 1
            except(KeyError):
                count_dict[order['day']] = 1
        return max(count_dict, key=count_dict.get)

    def get_least_busy_day(self):
        count_dict = {}
        for order in self.orders:
            try:
                count_dict[order['day']] += 1
            except(KeyError):
                count_dict[order['day']] = 1
        return min(count_dict, key=count_dict.get)
