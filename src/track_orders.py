class TrackOrders:

    # inicia a instancia
    def __init__(self):
        self.orders = []

# retorna o tamanho do array estanciado
    def __len__(self):
        return len(self.orders) or 0

    def new_order(self, customer, order, day):
        self.orders.append({'customer': customer, 'order': order, 'day': day})
        pass

    def most_order_food_by_customer(self, customer):
        counter = {}
        most = ""
        orders_by_custumer = filter(lambda o: o['customer']
                                    == customer, self.orders)

        for order in orders_by_custumer:
            is_food = order['order']
            if is_food not in counter:
                counter[is_food] = 1
            else:
                counter[is_food] += 1
            if most == "" or counter[is_food] > counter[most]:
                most = is_food

        return most

    def food_never_ordered(self, customer):
        all_foods = set()
        for order in self.orders:
            all_foods.add(order['order'])

        foods_ordered_by_customer = set()
        cust_order = filter(lambda o: o['customer'] == customer, self.orders)
        for order in cust_order:
            foods_ordered_by_customer.add(order['order'])

        return all_foods - foods_ordered_by_customer

    def never_date(self, customer):
        all_dates = set()
        for order in self.orders:
            all_dates.add(order['day'])

        customer_orders_by_date = set()
        filter_order = filter(lambda o: o['customer'] == customer, self.orders)
        for order in filter_order:
            customer_orders_by_date.add(order['day'])

        return all_dates - customer_orders_by_date
