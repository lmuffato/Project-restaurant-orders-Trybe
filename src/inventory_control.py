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
        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }


    def add_new_order(self, costumer, order, day):
        if order in InventoryControl.get_available_dishes(self):
            for item in InventoryControl.INGREDIENTS[order]:
                self.inventory[item] -= 1
            self.orders.append([costumer, order, day])
        else:
            return False


    def get_quantities_to_buy(self):
        ingredients_counter = {}

        for item in InventoryControl.MINIMUM_INVENTORY.keys():
            ingredients_counter[item] = 0

        for customer, product, day in self.orders:
            for item in InventoryControl.INGREDIENTS[product]:
                ingredients_counter[item] += 1

        return ingredients_counter


    def get_available_dishes(self):
        available_dishes = set()

        for dish in InventoryControl.INGREDIENTS.keys():
            available = True
            for item in InventoryControl.INGREDIENTS[dish]:
                if self.inventory[item] <= 0:
                    available = False

            if available:
                available_dishes.add(dish)

        return available_dishes
