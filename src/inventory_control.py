class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_quantities_to_buy(self):
        ingredients_counter = {}

        for item in InventoryControl.MINIMUM_INVENTORY.keys():
            ingredients_counter[item] = 0

        for customer, product, day in self.orders:
            for item in InventoryControl.INGREDIENTS[product]:
                ingredients_counter[item] += 1

        return ingredients_counter
