def get_max_order_client(orders, client):
    order_client = [order for order in orders if order["client"] == client]
    order_max = {}
    most_frequent = order_client[0]["order"]
    for order in order_client:
        food = order["order"]
        if food not in order_max:
            order_max[food] = 1
        else:
            order_max[food] += 1
        if order_max[food] > order_max[most_frequent]:
            most_frequent = food
    # print(most_frequent)
    return most_frequent


def get_not_ordered(orders, client):
    single_orders = {order["order"] for order in orders}
    order_client = (
        {order["order"] for order in orders if order["client"] == client})
    not_ordered = single_orders.difference(order_client)
    # print(not_ordered)
    return not_ordered


def get_not_days(orders, client):
    single_days = {order["day"] for order in orders}
    order_client = (
        {order["day"] for order in orders if order["client"] == client})
    not_days = single_days.difference(order_client)
    # print(not_days)
    return not_days


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {"client": costumer, "order": order, "day": day}
            )

    def get_most_ordered_dish_per_costumer(self, costumer):
        return get_max_order_client(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return get_not_ordered(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return get_not_days(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
