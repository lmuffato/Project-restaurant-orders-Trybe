from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {'customer_name': costumer, 'order': order, 'day': day})

    def filter_orders(self, costumer):
        data = self.orders
        cus_info = [dict for dict in data if dict['customer_name'] == costumer]
        return cus_info

    def get_most_ordered_dish_per_costumer(self, costumer):
        cus_order = self.filter_orders(costumer)
        all_orders = [single_dict['order'] for single_dict in cus_order]
        count = Counter(all_orders)
        most_ordered = count.most_common(1)[0][0]
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        cus_order = self.filter_orders(costumer)
        all_orders = [single_dict['order'] for single_dict in self.orders]
        customer_orders = [single_dict['order'] for single_dict in cus_order]
        all_orders_set = set(all_orders)
        customer_orders_set = set(customer_orders)
        return all_orders_set.difference(customer_orders_set)

    def get_days_never_visited_per_costumer(self, costumer):
        cus_order = self.filter_orders(costumer)
        days_open_restaurant = [dict['day'] for dict in self.orders]
        custumer_days_been = [single_dict['day'] for single_dict in cus_order]
        days_open_restaurant_set = set(days_open_restaurant)
        custumer_days_been_set = set(custumer_days_been)
        return days_open_restaurant_set.difference(custumer_days_been_set)
