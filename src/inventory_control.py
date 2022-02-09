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
    DISHES = {
        'hamburguer',
        'pizza',
        'misto-quente',
        'coxinha',
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

    def get_available_dishes(self):
        nao_tem = self.get_quantities_to_buy()
        acabou_ingrediente = dict()
        # comparar as chaves dos dois dic
        for key in self.MINIMUM_INVENTORY:
            if (key in nao_tem and self.MINIMUM_INVENTORY[key] == nao_tem[key]):
                acabou_ingrediente[key] = self.MINIMUM_INVENTORY[key]  # se igual a zero, verificar qual prato não pode ser feito
        for chave, valor in self.INGREDIENTS.items(): # .items() transforma numa lista de pares
            its_over = set(acabou_ingrediente)
            menu_ing = set(valor)
            z = its_over.intersection(menu_ing)
            if z != set():
               self.DISHES.remove(chave) 
        return self.DISHES # voltar uma lista com os pratos que podem ser feitos
       
       # bloquear o método add_new_order        
