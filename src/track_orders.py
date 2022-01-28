from src.analyze_log import get_data, get_frequency


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        my_foods = get_data(self.orders)[0]
        return get_frequency(my_foods[costumer])[1]

    def get_order_frequency_per_costumer(self, costumer1, customer2):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        my_foods, *_, dishes, _ = get_data(self.orders)
        *_, foods = get_frequency(my_foods[costumer])
        return dishes - foods

    def get_days_never_visited_per_costumer(self, costumer):
        _, my_days, *_, all_days = get_data(self.orders)
        *_, days = get_frequency(my_days[costumer])
        return all_days - days

    def get_list_days(self):
        _, my_days, *_ = get_data(self.orders)
        result = []

        for _, b in my_days.items():
            result += b

        return result

    def get_busiest_day(self):
        return get_frequency(self.get_list_days())[1]

    def get_least_busy_day(self):
        return get_frequency(self.get_list_days())[2]
