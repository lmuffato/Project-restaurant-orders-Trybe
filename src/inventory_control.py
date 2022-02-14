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
        self.menu = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        for ingredient in self.MINIMUM_INVENTORY.keys():
            self.ingredients[ingredient] = 0


    def remove_from_menu(self, ingredient, stock, ingredient_qty):
        if stock - ingredient_qty == 0:
            for key, value in self.INGREDIENTS.items():
                if ingredient in value and key in self.menu:
                    del self.menu[key]


    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        for ingredient in self.INGREDIENTS[order]:
            self.ingredients[ingredient] += 1

            ingredient_stock = self.MINIMUM_INVENTORY[ingredient]
            ingredient_qty = self.ingredients[ingredient]

            self.remove_from_menu(
                ingredient, ingredient_stock, ingredient_qty
            )

            if ingredient_stock - ingredient_qty < 0:
                return False


    def get_quantities_to_buy(self):
        return self.ingredients


    def get_available_dishes(self):
        return self.menu.keys()
