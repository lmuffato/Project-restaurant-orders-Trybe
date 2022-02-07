from collections import Counter


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
        self.lista_pedidos  = []

    def add_new_order(self, costumer, order, day):
        self.lista_pedidos.append({
            'customer': costumer,
            'order': order,
            'day': day
        })

    def get_quantities_to_buy(self):
        zero_ingredientes = {
        'pao': 0,
        'carne': 0,
        'queijo': 0,
        'molho': 0,
        'presunto': 0,
        'massa': 0,
        'frango': 0,
    }
        todos_ingre = []
        for row in self.lista_pedidos:
            pedidos = row['order']
            ingredientes = self.INGREDIENTS[pedidos]
            todos_ingre.extend(ingredientes)
        r = Counter(todos_ingre)
        for chave, valor in r.items():
            zero_ingredientes[chave] = valor
        return zero_ingredientes
