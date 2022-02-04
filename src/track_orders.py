class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_orders = [
            costumer_order["order"]
            for costumer_order in self.orders
            if costumer_order["costumer"] == costumer
        ]

        return max(customer_orders, key=customer_orders.count)

    def get_never_ordered_per_costumer(self, costumer):
        dishes = set(
            [costumer_order["order"] for costumer_order in self.orders]
        )

        costumer_orders = set(
            [
                costumer_order["order"]
                for costumer_order in self.orders
                if costumer_order["costumer"] == costumer
            ]
        )
        print(f"todos os pratos: {dishes}\npratos do cliente{costumer_orders}")

        return dishes.difference(costumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set([costumer_order["day"] for costumer_order in self.orders])

        costumer_days = set(
            [
                costumer_order["day"]
                for costumer_order in self.orders
                if costumer_order["costumer"] == costumer
            ]
        )

        return days.difference(costumer_days)

    def get_busiest_day(self):
        days = [order["day"] for order in self.orders]
        print("days:", days)
        return max(days, key=days.count)

    def get_least_busy_day(self):
        pass

    def clear(self):
        self.orders.clear()
