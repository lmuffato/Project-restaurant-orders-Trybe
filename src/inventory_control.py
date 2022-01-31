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

    def _verify_order_ingredients_availability(self, order):
        for order_ingredient in self.INGREDIENTS[order]:
            min_inventory = self.MINIMUM_INVENTORY[order_ingredient]
            if order_ingredient not in self.spent_ingredients:
                continue
            if self.spent_ingredients[order_ingredient] >= min_inventory:
                return False
        return True

    def add_new_order(self, costumer, order, day):
        if not self._verify_order_ingredients_availability(order):
            return False
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

    def _verify_unavailable_ingredients(self):
        unavailable_ingredients = []
        for ingredient in self.spent_ingredients.keys():
            min_stock = self.MINIMUM_INVENTORY[ingredient]
            if self.spent_ingredients[ingredient] >= min_stock:
                unavailable_ingredients.append(ingredient)
        return unavailable_ingredients

    def get_available_dishes(self):
        available_dishes = []
        unavailable_ingredients = self._verify_unavailable_ingredients()
        for dish in self.INGREDIENTS.keys():
            if len(set(self.INGREDIENTS[dish])
                    .intersection(unavailable_ingredients)) > 0:
                continue
            else:
                available_dishes.append(dish)
        return set(available_dishes)
