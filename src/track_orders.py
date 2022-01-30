class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        count_order = {}

        for register in self.orders:
            if register[0] == costumer:
                if register[1] not in count_order:
                    count_order[register[1]] = 1
                else:
                    count_order[register[1]] += 1

        return max(count_order, key=count_order.get)

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        customer_order = set()

        for register in self.orders:
            if register[1] not in all_orders:
                all_orders.add(register[1])

            if register[0] == costumer:
                if register[1] not in customer_order:
                    customer_order.add(register[1])

        return all_orders - customer_order

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        customer_day = set()

        for register in self.orders:
            if register[2] not in all_days:
                all_days.add(register[2])

            if register[0] == costumer:
                if register[2] not in customer_day:
                    customer_day.add(register[2])

        return all_days - customer_day

    def get_busiest_day(self):
        count_days = {}

        for register in self.orders:
            if register[2] not in count_days:
                count_days[register[2]] = 1
            else:
                count_days[register[2]] += 1

        return max(count_days, key=count_days.get)

    def get_least_busy_day(self):
        count_days = {}

        for register in self.orders:
            if register[2] not in count_days:
                count_days[register[2]] = 1
            else:
                count_days[register[2]] += 1

        return min(count_days, key=count_days.get)
