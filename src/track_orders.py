from collections import Counter


class TrackOrders:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        return self.data.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        data = self.data
        clients_orders = []
        for index in range(len(data)):
            if data[index][0] == costumer:
                clients_orders.append(data[index][1])
        most_requested = list(Counter(clients_orders))[1]
        return most_requested

    def get_never_ordered_per_costumer(self, costumer):
        data = self.data
        dishes_client = set()
        all_dishes = set()
        for index in range(len(data)):
            all_dishes.add(data[index][1])
            if data[index][0] == "joao":
                dishes_client.add(data[index][1])
        not_dishes_joao = all_dishes.difference(dishes_client)
        return not_dishes_joao

    def get_days_never_visited_per_costumer(self, costumer):
        data = self.data
        all_days = set()
        days_of_the_costumer = set()
        for index in range(len(data)):
            all_days.add(data[index][2])
            if data[index][0] == costumer:
                days_of_the_costumer.add(data[index][2])
        not_days_of_the_joao = all_days.difference(days_of_the_costumer)
        return not_days_of_the_joao

    def get_busiest_day(self):
        data = self.data
        result = self.data[0][2]
        busyest_days = {}

        for item in data:
            day = item[2]
            if day not in busyest_days:
                busyest_days[day] = 1
            else:
                busyest_days[day] += 1
            if busyest_days[result] < busyest_days[day]:
                result = day
        return result

    def get_least_busy_day(self):
        data = self.data
        result = self.data[0][2]
        busyest_days = {}

        for item in data:
            day = item[2]
            if day not in busyest_days:
                busyest_days[day] = 1
            else:
                busyest_days[day] += 1
            if busyest_days[result] > busyest_days[day]:
                result = day
        return result
