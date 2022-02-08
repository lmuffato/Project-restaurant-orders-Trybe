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
        self.quantities_to_buy = {
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
            if self.quantities_to_buy[ing] >= self.MINIMUM_INVENTORY[ing]:
                return False

            self.quantities_to_buy[ing] += 1

    def get_quantities_to_buy(self):
        return self.quantities_to_buy

    def get_available_dishes(self):
        available_dishes = set()
        for dish, ingredients in self.INGREDIENTS.items():
            is_available = True
            for ing in ingredients:
                if self.quantities_to_buy[ing] >= self.MINIMUM_INVENTORY[ing]:
                    is_available = False

            if is_available:
                available_dishes.add(dish)

        return available_dishes
