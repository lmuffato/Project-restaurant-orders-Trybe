from collections import Counter


class TrackOrders:
    def __init__(self):
        self.order_data = []

    def __len__(self):
        return len(self.order_data)

    def filter(self, costumer):
        customer_order = [
            order["order"]
            for order in self.order_data
            if order["customer"] == costumer
        ]
        return customer_order

    def add_new_order(self, costumer, order, day):
        self.order_data.append({
            "customer": costumer,
            "order": order,
            "weekday": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_order = self.filter(costumer)
        count = Counter(customer_order)
        most_ordered_dish = count.most_common(1)[0][0]
        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        menu = {orders["order"] for orders in self.order_data}
        customer_order = self.filter(costumer)
        dishes_without_orders = menu.symmetric_difference(customer_order)
        return dishes_without_orders

    def get_days_never_visited_per_costumer(self, costumer):
        weekdays = {orders["weekday"] for orders in self.order_data}
        days_by_customer = {
            orders["weekday"]
            for orders in self.order_data
            if orders["customer"] == costumer
        }
        absence_days = weekdays.symmetric_difference(days_by_customer)
        return absence_days

    def get_busiest_day(self):
        weekdays = [orders["weekday"] for orders in self.order_data]
        count = Counter(weekdays)
        busiest_day = max(count, key=count.get)
        return busiest_day

    def get_least_busy_day(self):
        weekdays = [orders["weekday"] for orders in self.order_data]
        count = Counter(weekdays)
        least_busy_day = min(count, key=count.get)
        return least_busy_day
