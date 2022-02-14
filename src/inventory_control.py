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
        self.ingredients = dict()

        for ingredient in self.MINIMUM_INVENTORY.keys():
            self.ingredients[ingredient] = 0

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        for ingredient in self.INGREDIENTS[order]:
            self.ingredients[ingredient] += 1

    def get_quantities_to_buy(self):
        return self.ingredients
