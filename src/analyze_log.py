import csv


def read_csv(path):
    result = []
    with open(path) as file:
        data_reader = csv.reader(file)
        for name, food, day in data_reader:
            result.append(
                {
                    "name": name,
                    "food": food,
                    "day": day,
                }
            )
    return result


def prato_mais_pedido(data, costumer):
    dicionario = dict()
    for i in data:
        if i["name"] == costumer:
            if i["food"] not in dicionario:
                dicionario[i["food"]] = 1
            else:
                dicionario[i["food"]] += 1
    result = max(dicionario, key=dicionario.get)
    return result


def arnaldo_hamburger_count(data):
    counter = 0
    for i in data:
        if i["name"] == "arnaldo":
            if i["food"] == "hamburguer":
                counter += 1
    print(counter)
    return counter


def food_never_requested(data, costumer):
    requested_foods = set()
    for i in data:
        if i["name"] == costumer:
            requested_foods.add(i["food"])
    all_foods = set([i["food"] for i in data])
    not_requested = all_foods.difference(requested_foods)
    return not_requested


def days_never_visited(data, costumer):
    all_days = set([i["day"] for i in data])
    joao_days_on = set()
    for i in data:
        if i["name"] == costumer:
            joao_days_on.add(i["day"])
    return all_days.difference(joao_days_on)


def write_in_txt(text, txt_file):
    with open(txt_file, "w") as file:
        file.write(text)


def analyze_log(path_to_file):
    data = read_csv(path_to_file)
    favorite_food = prato_mais_pedido(data, "maria")
    arnaldo_pedido = arnaldo_hamburger_count(data)
    joao_nao_pediu = food_never_requested(data, "joao")
    joao_nao_veio = days_never_visited(data, "joao")
    text = (
        f"{favorite_food}\n"
        + f"{arnaldo_pedido}\n"
        + f"{joao_nao_pediu}\n"
        + f"{joao_nao_veio}"
    )
    write_in_txt(text, "data/mkt_campaign.txt")
