from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        new_order = {'customer': customer, "order": order, "day": day}

        self.orders.append(new_order)

    def get_orders_per_costumer(self, customer):
        filtered_data = [
          item for item in self.orders if item["customer"] == customer
          ]

        return filtered_data

    def get_most_ordered_dish_per_costumer(self, customer):
        filtered_order = self.get_orders_per_costumer(customer)

        filtered_data = [item["order"] for item in filtered_order]
        count_order = Counter(filtered_data)

        return count_order.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, customer):
        filtered_order = self.get_orders_per_costumer(customer)

        general_order = set([item["order"] for item in self.orders])
        customer_order = set([item["order"] for item in filtered_order])

        return general_order.difference(customer_order)

    def get_days_never_visited_per_costumer(self, customer):
        filtered_order = self.get_orders_per_costumer(customer)

        general_order = set([item["day"] for item in self.orders])
        customer_order = set([item["day"] for item in filtered_order])

        return general_order.difference(customer_order)

    def get_busiest_day(self):
        day_order = self.orders[0]["day"]
        count_order = {}

        for item in self.orders:
            if item["day"] not in count_order:
                count_order[item["day"]] = 1
            else:
                count_order[item["day"]] += 1

            if count_order[item["day"]] > count_order[day_order]:
                day_order = item["day"]

        return day_order

    def get_least_busy_day(self):
        day_order = self.orders[0]["day"]
        count_order = {}

        for item in self.orders:
            if item["day"] not in count_order:
                count_order[item["day"]] = 1
            else:
                count_order[item["day"]] += 1

            if count_order[item["day"]] < count_order[day_order]:
                day_order = item["day"]

        return day_order

# Os últimos methods foram refatorados usando de base o exercício 6 de
# fixação do bloco 36.3, onde ele mostra o uso de um contador manual.

# Obs: tive que refatorar e deixar o uso do Count de lado, pois
# os requisitos passavam x vezes sim e outras falhavam.
