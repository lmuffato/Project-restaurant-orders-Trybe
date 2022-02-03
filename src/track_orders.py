from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add_new_order(self, costumer, order, day):
        self.order.append({"costumer": costumer, "order": order, "day": day})
        return self.order

    def get_most_ordered_dish_per_costumer(self, costumer):
        list_costumer = []
        for item_list in self.order:
            if item_list["costumer"] == costumer:
                list_costumer.append(item_list["order"])
                dict_count = Counter(list_costumer)
                result = dict_count.most_common(1)
        return result[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        list_costumer = set()
        list_all_dishes = set()
        for item_list in self.order:
            list_all_dishes.add(item_list["order"])
            if item_list["costumer"] == costumer:
                list_costumer.add(item_list["order"])
        result = list_all_dishes - list_costumer
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        list_costumer = set()
        list_all_days = set()
        for item_list in self.order:
            list_all_days.add(item_list["day"])
            if item_list["costumer"] == costumer:
                list_costumer.add(item_list["day"])
        result = list_all_days - list_costumer
        return result

    def get_busiest_day(self):
        list_days = []
        for item_list in self.order:
            list_days.append(item_list["day"])
            dict_count = Counter(list_days)
            result = dict_count.most_common(1)
        return result[0][0]

    def get_least_busy_day(self):
        list_days = []
        for item_list in self.order:
            list_days.append(item_list["day"])
            dict_count = Counter(list_days)
            len(dict_count)
            result = dict_count.most_common()
        return result[len(dict_count) - 1][0]
