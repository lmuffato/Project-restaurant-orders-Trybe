# Requisito 2 feito com ajuda do Jodiel

class TrackOrders:

    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        quantity_ordered = 1
        dish_name = self.orders[0][1]

        for item in self.orders:
            dish = item[1]
            client = item[0]

            if client == costumer:
                if dish not in count:
                    count[dish] = 1
                else:
                    count[dish] += 1

                if count[dish] > quantity_ordered:
                    quantity_ordered = count[dish]
                    dish_name = dish

        return dish_name

    def get_never_ordered_per_costumer(self, costumer):
        pass

# uso do add - https://www.geeksforgeeks.org/set-add-python/

    def get_days_never_visited_per_costumer(self, costumer):
        days_of_the_week = set()
        visited_days = set()
        for item in self.orders:
            day = item[2]
            client = item[0]
            days_of_the_week.add(day)
            if client == costumer:
                visited_days.add(day)
        return days_of_the_week.difference(visited_days)

    def get_busiest_day(self):
        result = self.orders[0][2]
        busy_days = {}

        for item in self.orders:
            day = item[2]
            if day not in busy_days:
                busy_days[day] = 1
            else:
                busy_days[day] += 1
            if busy_days[result] < busy_days[day]:
                result = day
        return result

    def get_least_busy_day(self):
        result = self.orders[0][2]
        not_busy_days = {}

        for item in self.orders:
            day = item[2]
            if day not in not_busy_days:
                not_busy_days[day] = 1
            else:
                not_busy_days[day] += 1
            if not_busy_days[result] > not_busy_days[day]:
                result = day
        return result
