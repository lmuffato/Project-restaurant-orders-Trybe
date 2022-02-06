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
        self.inventory = self.MINIMUM_INVENTORY

    def add_new_order(self, costumer, order, day):
        if order not in self.get_available_dishes():
            return False
        else:
            self.orders.append([costumer, order, day])

    def get_quantities_to_buy(self):
        qtties_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

        for order in self.orders:
            ingredients = self.INGREDIENTS[order[1]]
            for ingredient in ingredients:
                qtties_to_buy[ingredient] += 1

        return qtties_to_buy

    def get_available_dishes(self):
        available_dishes = set()
        for dish, ingredients in self.INGREDIENTS.items():
            is_available = True

            for ingredient in ingredients:
                if self.inventory[ingredient] == 0:
                    is_available = False

            if is_available:
                available_dishes.add(dish)

        return available_dishes
