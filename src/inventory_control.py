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
        self.inventory = self.MINIMUM_INVENTORY.copy()
        self.recipes = self.INGREDIENTS.copy()

    def add_new_order(self, costumer, order, day):
        order_success = None
        for ingredient in self.recipes[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                order_success = False
        self.orders.append(
            {"costumer": costumer, "order": order, "day": day}
        )
        return order_success

    def get_quantities_to_buy(self):
        buy_list = {item: 0 for item in self.inventory}
        for order in self.orders:
            for ingredient in self.recipes[order["order"]]:
                buy_list[ingredient] += 1
        return buy_list

    def get_available_dishes(self):
        recipes = set()
        no_ingredient = set()
        for ingredient in self.inventory:
            if self.inventory[ingredient] == 0:
                no_ingredient.add(ingredient)
        for recipe in self.recipes:
            if len(
                no_ingredient.intersection(set(self.recipes[recipe]))
            ) == 0:
                recipes.add(recipe)
        return recipes
