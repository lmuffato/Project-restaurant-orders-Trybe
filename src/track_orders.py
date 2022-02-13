class TrackOrders:

    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)


    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])


    def get_most_ordered_dish_per_costumer(self, costumer):
        result = [row[1] for row in self.orders if row[0] == costumer]

        # for row in self.orders:
        #     if row[0] == costumer:
        #         result.append(row[1])
        return max(result, key=result.count)


    def get_never_ordered_per_costumer(self, costumer):
        all_foods = [row[1] for row in self.orders]
        foods_ordered_by_customer = [row[1] for row in self.orders if row[0] == costumer]

        # for row in self.orders:
        #     if row[0] == costumer:
        #         foods_ordered_by_customer.append(row[1])
        return set(all_foods) - set(foods_ordered_by_customer)
        

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = [row[2] for row in self.orders]
        days_customer_ordered = [row[2] for row in self.orders if row[0] == costumer]

        # for row in self.orders:
        #     if row[0] == costumer:
        #         days_customer_ordered.append(row[2])
        return set(all_days) - set(days_customer_ordered)


    def get_busiest_day(self):
        all_days = [data[2] for data in self.orders]
        return max(all_days, key=all_days.count)


    def get_least_busy_day(self):
        all_days = [data[2] for data in self.orders]
        return min(all_days, key=all_days.count)
