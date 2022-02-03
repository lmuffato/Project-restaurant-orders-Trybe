from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orderList = self.orders
        clientOrder = []
        for i in range(len(orderList)):
            if orderList[i][0] == costumer:
                clientOrder.append(orderList[i][1])
        return list(Counter(clientOrder))[1]

    def get_never_ordered_per_costumer(self, costumer):
        orderList = self.orders
        menuClient = set()
        allMenu = set()
        for i in range(len(orderList)):
            allMenu.add(orderList[i][1])
            if orderList[i][0] == costumer:
                menuClient.add(orderList[i][1])
        return allMenu.difference(menuClient)

    def get_days_never_visited_per_costumer(self, costumer):
        orderList = self.orders
        clientDay = set()
        allDays = set()
        for i in range(len(orderList)):
            allDays.add(orderList[i][2])
            if orderList[i][0] == costumer:
                clientDay.add(orderList[i][2])
        return allDays.difference(clientDay)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
