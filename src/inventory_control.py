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
        self.ingredients_to_buy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }


    # ADICIONA UM NOVO PEDIDO
    def add_new_order(self, costumer, order, day):
        # para cada ingrediente da lista de ingredientes
        for ingredient in self.INGREDIENTS[order]:
            # se o ingrediente da lista de compras for maior
            # ou igual ao disponível, retorna falso
            if self.ingredients_to_buy[ingredient] >= (
              self.MINIMUM_INVENTORY[ingredient]):
                return False
            # se não, adiciona 1 ao valor do ingrediente
            self.ingredients_to_buy[ingredient] += 1

    # RETORNA A LISTA DE INGREDIENTES PRA COMPRAR
    def get_quantities_to_buy(self):

        return self.ingredients_to_buy

    # RETORNA OS PRATOS DISPONÍVEIS
    def get_available_dishes(self):
        # cria uma lista de objetos únicos
        receitas_disponiveis = set()

        # para cada comida e array de ingredientes
        for food, ingredients in self.INGREDIENTS.items():

            ingrediente_disponivel = True
            # pra cada ingrediente na lista
            for ingrediente in ingredients:

                # se o ingrediente pra comprar for maior que o disponível
                # necessário ao ingrediente retorna falso
                if self.ingredients_to_buy[ingrediente] >= (
                  self.MINIMUM_INVENTORY[ingrediente]):
                    ingrediente_disponivel = False

            # Se o ingrediente está disponível, o nome do prato
            # vai para a lista de receitas disponíveis
            if ingrediente_disponivel:
                receitas_disponiveis.add(food)

        return receitas_disponiveis


# Teste automatizado
# python3 -m pytest tests/inventory_control.py

# Teste manual
# inventory_control = InventoryControl()

# inventory_control.add_new_order('Maria', 'hamburguer', 'sexta-feira')

# print(inventory_control.get_quantities_to_buy())

# Testando a indisponibilidade de receitas
# for x in range(50):
#   inventory_control.add_new_order('Maria', 'hamburguer', 'sexta-feira')  

# print(inventory_control.get_available_dishes())
