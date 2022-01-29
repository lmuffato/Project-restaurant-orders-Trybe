import src.analyze_log as analyze_log


class TrackOrders:
    def __init__(self):
        self.requests = []

    def __len__(self):
        return len(self.requests)

    def add_new_order(self, costumer, order, day):
        self.requests.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return analyze_log.most_request_dish(self.requests, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        result = analyze_log.dishes_never_asked(self.requests, costumer)
        # print(result)
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        days_of_week = [requests[2] for requests in self.requests]
        for requests in self.requests:
            if requests[0] == costumer:
                for day in days_of_week:
                    if day == requests[2]:
                        days_of_week.remove(day)

        print(days_of_week)

        return set(days_of_week)

    def get_busiest_day(self):
        days_of_week = [requests[2] for requests in self.requests]
        return max(set(days_of_week), key=days_of_week.count)

    def get_least_busy_day(self):
        days_of_week = [requests[2] for requests in self.requests]
        return min(set(days_of_week), key=days_of_week.count)
