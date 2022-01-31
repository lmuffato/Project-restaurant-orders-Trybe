from track_orders import TrackOrders


class InventoryControl:
    # INITIAL_INVENTORY
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
        self.ingredients_to_use = self.MINIMUM_INVENTORY.copy()  # shallow copy

    def add_new_order(self, costumer, order, day):
        for item in self.INGREDIENTS[order]:
            if self.ingredients_to_use[item] < 1:
                return False
            else:
                new_order = TrackOrders()
                new_order.add_new_order(costumer, order, day)
                self.ingredients_to_use[item] -= 1

    def get_quantities_to_buy(self):
        need_to_buy = {}
        for ingredient in self.MINIMUM_INVENTORY:
            need_to_buy[ingredient] = (
                self.MINIMUM_INVENTORY[ingredient]
                - self.ingredients_to_use[ingredient]
            )
        return need_to_buy

    def get_available_dishes(self):
        current_available_dishes = set()

        for meal in self.INGREDIENTS:
            curr_ingredients = self.INGREDIENTS[meal]
            for ingredient in curr_ingredients:
                print(meal, ingredient)
                if self.ingredients_to_use[ingredient] < 1:
                    break
                else:
                    current_available_dishes.add(meal)
        return current_available_dishes
