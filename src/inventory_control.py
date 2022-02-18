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
        self.shop_list = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        for ing in self.INGREDIENTS[order]:
            if self.shop_list[ing] >= self.MINIMUM_INVENTORY[ing]:
                return False
            self.shop_list[ing] += 1

    def get_quantities_to_buy(self):
        return self.shop_list

    def get_available_dishes(self):
        available_meals = set()
        missing_ingredient = set()
        for ing in self.MINIMUM_INVENTORY:
            if self.MINIMUM_INVENTORY[ing] == 0:
                missing_ingredient.add(ing)
        for meal in self.INGREDIENTS:
            if len(
                missing_ingredient.intersection(set(self.INGREDIENTS[meal]))
            ) == 0:
                available_meals.add(meal)
        return available_meals
