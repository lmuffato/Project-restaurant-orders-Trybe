class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self._orders = []
        self._used_ingredients = dict()
        self._menu = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }

        for ingredient in self.MINIMUM_INVENTORY.keys():
            self._used_ingredients[ingredient] = 0

    def add_new_order(self, costumer, order, day):
        self._orders.append([costumer, order, day])
        for ingredient in self.INGREDIENTS[order]:
            self._used_ingredients[ingredient] += 1

            ingredient_stock = self.MINIMUM_INVENTORY[ingredient]
            used_ingredient_qty = self._used_ingredients[ingredient]

            if ingredient_stock - used_ingredient_qty < 0:
                return False

    def get_quantities_to_buy(self):
        return self._used_ingredients

    def get_available_dishes(self):
        return self._menu.keys()
