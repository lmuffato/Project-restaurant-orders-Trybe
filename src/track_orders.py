class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append(
            {"cliente": costumer, "pedido": order, "dia": day}
        )

    def get_orders_per_costumer(self, costumer):
        filtered_orders = []
        for order in self.orders:
            if order["cliente"] == costumer:
                filtered_orders.append(order)
        return filtered_orders

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = self.get_orders_per_costumer(costumer)
        most_ordered_dish = {}
        for order in costumer_orders:
            if order["pedido"] in most_ordered_dish:
                most_ordered_dish[order["pedido"]] += 1
            else:
                most_ordered_dish[order["pedido"]] = 1
        return max(most_ordered_dish, key=most_ordered_dish.get)

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass


teste = TrackOrders()

teste.add_new_order("madruga", "pizza", "sabadão")
teste.add_new_order("madruga", "pizza", "sabadão")
teste.add_new_order("madruga", "miojo frito", "domingão")
teste.add_new_order("vanessa", "coxinha", "segunda-feira")
print(teste.orders)
print(teste.__len__())

print('===== FILTRA AS ORDERNS POR CLIENTE =====')
print(teste.get_orders_per_costumer("madruga"))

print('===== FILTRA A COMIDA MAIS PEDIDA POR CLIENTE =====')
print(teste.get_most_ordered_dish_per_costumer("madruga"))
