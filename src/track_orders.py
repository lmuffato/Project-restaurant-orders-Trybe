class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)
        # pass

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])
        # pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_dishes = []

        for element in self.orders:
            if element[0] == costumer:
                costumer_dishes.append(element[1])
        return max(set(costumer_dishes), key=costumer_dishes.count)
        # pass

    def get_never_ordered_per_costumer(self, costumer):
        ordered_by_costumer = []
        all_dishes = []

        for element in self.orders:
            if element[0] == costumer:
                ordered_by_costumer.append(element[1])
            else:
                all_dishes.append(element[1])

        difference = set(all_dishes).difference(set(ordered_by_costumer))
        return difference
        # pass

    def get_days_never_visited_per_costumer(self, costumer):
        visited_days_costumer = []
        all_work_days = []

        for element in self.orders:
            if element[0] == costumer:
                visited_days_costumer.append(element[2])
            else:
                all_work_days.append(element[2])

        difference = set(all_work_days).difference(set(visited_days_costumer))
        return difference
        # pass

    def get_busiest_day(self):
        days = []

        for element in self.orders:
            days.append(element[2])
        return max(set(days), key=days.count)
        # pass

    def get_least_busy_day(self):
        days = []

        for element in self.orders:
            days.append(element[2])
        return min(set(days), key=days.count)
        # pass
