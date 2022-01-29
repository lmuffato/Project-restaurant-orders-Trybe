from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {'costumer': costumer, 'order': order, 'weekday': day})

    def filter_orders(self, costumer):
        data = self.orders
        filtered_data = [d for d in data if d['costumer'] == costumer]
        return filtered_data

    def get_most_ordered_dish_per_costumer(self, costumer):
        filtered_costumer = self.filter_orders(costumer)
        filtered_data = [d['order'] for d in filtered_costumer]
        count = Counter(filtered_data)
        return count.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        filtered_costumer = self.filter_orders(costumer)
        filtered_data = [d['order'] for d in self.orders]
        custumer_filter = [d['order'] for d in filtered_costumer]
        return (set(filtered_data)-set(custumer_filter))

    def get_days_never_visited_per_costumer(self, costumer):
        filtered_costumer = self.filter_orders(costumer)
        filtered_data = [d['weekday'] for d in self.orders]
        custumer_filter = [d['weekday'] for d in filtered_costumer]
        return (set(filtered_data)-set(custumer_filter))

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
