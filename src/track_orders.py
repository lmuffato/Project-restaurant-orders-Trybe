class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = []
        for order in self.orders:
            if orders[0] == costumer:
                costumer_orders.append(orders[1])
        most_ordered = get_most_ordered_food(costumer_orders)
        return most_ordered

    def get_never_ordered_per_costumer(self, costumer):
        all_foods_repeted = []
        all_foods = []
        foods = []
        for order in self.orders:
            if orders[0] == costumer:
                foods.append(orders[1])
            all_foods_repeted.append(orders[1])
        for food in all_foods_repeted:
            if food not in all_foods:
                all_foods.append(food)
        never_ordered = never_ordered_customer(all_foods, foods)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        all_days_repeated = []
        all_days = []
        costumer_days = []
        for order in self.orders:
            if order[0] == costumer:
                costumer_days.append(order[2])
            all_days_repeated.append(order[2])

        for day in all_days_repeated:
            if day not in all_days:
                all_days.append(day)
        never_visited = costumer_never_visited(all_days, costumer_days)
        return never_visited

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(orders[2])
        busiest = get_most_ordered_food(days)
        return busiest

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(orders[2])
        least_busy = get_least_ordered(days)
        return least_busy


def get_most_ordered_food(foods):
    count_foods = {}
    most_frequent = foods[0]

    for food in foods:
        if food not in count_foods:
            count_foods[food] = 1
        else:
            count_foods[food] += 1

        if count_foods[food] > count_foods[most_frequent]:
            most_frequent = food

    return most_frequent


def never_ordered_customer(all_foods, joao_foods):
    not_ordered = set()
    for foods in all_foods:
        if foods not in joao_foods:
            not_ordered.add(foods)

    return not_ordered


def costumer_never_visited(all_days, costumer_days):
    never = set()
    for day in all_days:
        if day not in costumer_days:
            never.add(day)
    return never


def get_least_ordered(costumer_orders):
    least_ordered = costumer_orders[0]
    count = {}
    for order in costumer_orders:
        if order not in count:
            count[order] = 1
        else:
            count[order] += 1

        if count[order] < count[least_ordered]:
            least_ordered = order
    return least_ordered
