class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"client": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = dict()
        for row in self.orders:
            if row["client"] == costumer:
                if row["order"] not in ordered:
                    ordered[row["order"]] = 1
                else:
                    ordered[row["order"]] += 1
        result = max(ordered, key=ordered.get)
        return result

    def get_never_ordered_per_costumer(self, costumer):
        filter = []
        for row in self.orders:
            client_ = row["client"]
            if costumer == client_:
                filter.append(row)

        ordered_by_clients = set([row['order'] for row in self.orders])
        ordered_by_client = set([row['order'] for row in filter])
        return ordered_by_clients.difference(ordered_by_client)

    def get_days_never_visited_per_costumer(self, costumer):
        filter = []
        for row in self.orders:
            client_ = row["client"]
            if costumer == client_:
                filter.append(row)

        frequented_by_clients = set([row['day'] for row in self.orders])
        frequented_by_client = set([row['day'] for row in filter])
        return frequented_by_clients.difference(frequented_by_client)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
