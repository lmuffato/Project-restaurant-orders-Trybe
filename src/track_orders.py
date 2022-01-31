from typing import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        # precisava ter um id novo né? Mas não vamos complicar
        new_order = {"costumer": costumer, "order": order, "day": day}
        self.orders.append(new_order)
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_all_orders = Counter(
            order["order"]
            for order in self.orders
            if order["costumer"] == costumer
        )
        return max(costumer_all_orders, key=costumer_all_orders.get)

    def get_never_ordered_per_costumer(self, costumer):
        every_ordered_meal = Counter([order["order"] for order in self.orders])
        person_ordered_meals = Counter(
            [
                order["order"]
                for order in self.orders
                if order["costumer"] == costumer
            ]
        )
        list_difference = [
            meal
            for meal in every_ordered_meal
            if meal not in person_ordered_meals
        ]

        return set(list_difference)

    def get_days_never_visited_per_costumer(self, costumer):
        every_ordered_days = Counter([order["day"] for order in self.orders])
        person_ordered_days = Counter(
            [
                order["day"]
                for order in self.orders
                if order["costumer"] == costumer
            ]
        )
        list_difference = [
            day for day in every_ordered_days if day not in person_ordered_days
        ]
        return set(list_difference)

    def get_busiest_day(self):
        all_days = Counter(order["day"] for order in self.orders)
        return max(all_days, key=all_days.get)

    def get_least_busy_day(self):
        all_days = Counter(order["day"] for order in self.orders)
        return min(all_days, key=all_days.get)
