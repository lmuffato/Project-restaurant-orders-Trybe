from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add_new_order(self, costumer, order, day):
        self.order.append({"costumer": costumer, "order": order, "day": day})
        print(self.order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_costumer = []
        for item_list in self.order:
            if item_list["costumer"] == costumer:
                list_costumer.append(item_list["order"])
                dict_pop = Counter(list_costumer)
                result = dict_pop.most_common(1)
        return result[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
