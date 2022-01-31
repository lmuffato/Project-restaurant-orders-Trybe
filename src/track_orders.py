import src.analyze_log as util


class TrackOrders:
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add_new_order(self, costumer, order, day):
        self.order.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        return util.most_requested_food_by_customer(self.order, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return util.customer_never_ordered_food(self.order, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return util.customer_never_went_to_lanchonete(self.order, costumer)

    def get_busiest_day(self):
        return util.busiest_day(self.order)

    def get_least_busy_day(self):
        return util.least_busy_day(self.order)


"""a"""
