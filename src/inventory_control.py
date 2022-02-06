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
        self.inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, costumer, order, day):
        for ingre in self.INGREDIENTS[order]:
            if self.inventory[ingre] >= self.MINIMUM_INVENTORY[ingre]:
                return False
            self.inventory[ingre] += 1

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        dishes = ['hamburguer', 'pizza', 'misto-quente', 'coxinha']
        available_dishes = set()
        for dish in dishes:
            count = 0
            for ing in self.INGREDIENTS[dish]:
                if self.MINIMUM_INVENTORY[ing] <= self.inventory[ing]:
                    count += 1
            if count == 0:
                available_dishes.add(dish)
        return available_dishes
