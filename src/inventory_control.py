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
        self.spent_ingredients = {}

    def add_new_order(self, costumer, order, day):
        self.orders.append({costumer, order, day})
        for ingredient in self.INGREDIENTS[order]:
            if ingredient in self.spent_ingredients:
                self.spent_ingredients[ingredient] += 1
            else:
                self.spent_ingredients[ingredient] = 1

    def get_quantities_to_buy(self):
        stock_report = {}
        for ingredient in self.MINIMUM_INVENTORY.keys():
            min_stock = self.MINIMUM_INVENTORY[ingredient]
            if ingredient in self.spent_ingredients:
                buy = min_stock - self.spent_ingredients[ingredient]
                stock_report[ingredient] = min_stock - buy
            else:
                stock_report[ingredient] = 0
        return stock_report
