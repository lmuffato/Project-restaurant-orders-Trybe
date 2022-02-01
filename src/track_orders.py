from collections import Counter


class TrackOrders:
    data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        order_agg = self.aggregate_person_by(customer, 'order')
        return max(
            order_agg,
            key=lambda x: order_agg[x]
        )

    def get_never_ordered_per_customer(self, customer):
        customer_orders = set(self.aggregate_person_by(customer, 'order'))
        all_foods = self.get_all_foods()
        return set.difference(all_foods, customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        days_agg = set(self.aggregate_person_by(customer, 'day'))
        all_days = self.get_all_days()
        return set.difference(all_days, days_agg)

    def get_busiest_day(self):
        agg_days = Counter([x['day'] for x in self.data])
        busiest_day = max(agg_days, key=lambda x: agg_days[x])
        return busiest_day

    def get_least_busy_day(self):
        agg_days = Counter([x['day'] for x in self.data])
        unbusiest_day = min(agg_days, key=lambda x: agg_days[x])
        return unbusiest_day

    # custom
    def get_all_days(self):
        return set([x["day"] for x in self.data])

    def get_all_foods(self):
        return set([x["order"] for x in self.data])

    def aggregate_person_by(self, customer, key):
        return dict(Counter(
            [
                y[key] for y in [
                    x for x in self.data if x["customer"] == customer
                    ]
            ])
        )

    # typos methods
    def get_most_ordered_dish_per_costumer(self, customer):
        return self.get_most_ordered_dish_per_customer(customer)

    def get_never_ordered_per_costumer(self, customer):
        return self.get_never_ordered_per_customer(customer)

    def get_days_never_visited_per_costumer(self, customer):
        return self.get_days_never_visited_per_customer(customer)
