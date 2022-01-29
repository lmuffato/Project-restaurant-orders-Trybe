class TrackOrders:
    def __init__(self):
        self.orders_list = []

    def __len__(self):
        return len(self.orders_list)

    def add_new_order(self, costumer, order, day):
        self.orders_list.append(
            (costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        food_dict = {}
        for row in self.orders_list:
            if(row[0] == costumer):
                if(row[1] not in food_dict):
                    food_dict[row[1]] = 1
                else:
                    food_dict[row[1]] += 1
        return max(food_dict, key=food_dict.get)

    def get_never_ordered_per_costumer(self, costumer):
        dishes = {row[1] for row in self.orders_list}
        client_dishes = set(
            [row[1] for row in self.orders_list if row[0] == costumer])
        return client_dishes.symmetric_difference(dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        days = {row[2] for row in self.orders_list}
        days_client_went = set(
            [row[2] for row in self.orders_list if row[0] == costumer])
        return days_client_went.symmetric_difference(days)

    def get_busiest_day(self):
        days = {}
        for row in self.orders_list:
            if(row[2] not in days):
                days[row[2]] = 1
            else:
                days[row[2]] += 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for row in self.orders_list:
            if(row[2] not in days):
                days[row[2]] = 1
            else:
                days[row[2]] += 1
        return min(days, key=days.get)
