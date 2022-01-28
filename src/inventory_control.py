from functools import reduce
from typing import Counter


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
        self.orders = []

    def add_new_order(self, costumer, order, day):
        if order in self.get_available_dishes():
            self.orders.append(
                {"costumer": costumer, "order": order, "day": day}
            )
            return True
        return False

    def get_quantities_to_buy(self):
        ingredients_per_order = map(
            lambda order: self.INGREDIENTS[order["order"]], self.orders
        )

        def flat_map(f, xs):
            return reduce(lambda acc, cur: acc + cur, map(f, xs), [])
        ingredientes_all_orders = flat_map(lambda x: x, ingredients_per_order)
        count_ingredients = Counter(ingredientes_all_orders)
        MINIMUM_INVENTORY = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }
        return reduce(
            lambda acc, cur: {**acc, cur[0]: cur[1]},
            count_ingredients.items(),
            MINIMUM_INVENTORY,
        )

    def get_available_dishes(self):
        used_inventory = self.get_quantities_to_buy()
        available_ingredients = {
            k: self.MINIMUM_INVENTORY[k] - used_inventory[k]
            for k in self.MINIMUM_INVENTORY
        }
        available_dishes = set()
        for dish, ingredients in self.INGREDIENTS.items():
            is_available = True
            for ingredient in ingredients:
                if available_ingredients[ingredient] == 0:
                    is_available = False
            if is_available:
                available_dishes.add(dish)
        return available_dishes


inventory = InventoryControl()
count = 1
while count <= 50:
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("maria", "pizza", "terça-feira")
    count += 1
print(inventory.get_available_dishes())
hamburguer_pizza = inventory.add_new_order(
    "jorge", "hamburguer", "terça-feira"
)
