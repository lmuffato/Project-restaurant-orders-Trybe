class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
        'pizza': ['massa', 'queijo', 'molho'],
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
        self.available_dishes = set(self.INGREDIENTS)
        self.unavailable_ingredients = set()
        self.ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def get_available_dishes(self):
        for meal, ingredients in self.INGREDIENTS.items():
            ing_set = set(ingredients)
            is_unavailable = self.unavailable_ingredients.intersection(ing_set)
            if is_unavailable:
                self.available_dishes.remove(meal)
        return self.available_dishes

    def add_new_order(self, costumer, order, day):
        ingredients = self.INGREDIENTS[order]
        available = True
        for ing in ingredients:
            self.ingredients_to_buy[ing] += 1
            if (self.ingredients_to_buy[ing] == self.MINIMUM_INVENTORY[ing]):
                self.unavailable_ingredients.add(ing)
            if (self.ingredients_to_buy[ing] > self.MINIMUM_INVENTORY[ing]):
                self.ingredients_to_buy[ing] -= 1
                available = False

        if available:
            return self.orders.append({
                'cliente': costumer,
                'pedido': order,
                'dia': day,
            })
        return available

    def get_quantities_to_buy(self):
        return self.ingredients_to_buy
