import csv


def read_csv(path):
    result = []
    if path.endswith(".csv"):
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


def maria_mais_pedido(path):
    dicionario = dict()
    data_reader = read_csv(path)
    for i in data_reader:
        if i["name"] == "maria":
            if i["food"] not in dicionario:
                dicionario[i["food"]] = 1
            else:
                dicionario[i["food"]] += 1
    result = max(dicionario, key=dicionario.get)
    return result


def arnaldo_hamburger_count(path):
    data_reader = read_csv(path)
    counter = 0
    for i in data_reader:
        if i["name"] == "arnaldo":
            if i["food"] == "hamburguer":
                counter += 1
    print(counter)
    return counter


def joao_never_requested(path):
    data_reader = read_csv(path)
    requested_foods = set()
    for i in data_reader:
        if i["name"] == "joao":
            requested_foods.add(i["food"])
    all_foods = set([i["food"] for i in data_reader])
    not_requested = all_foods.difference(requested_foods)
    return not_requested


def joao_days_of(path):
    data_reader = read_csv(path)
    all_days = set([i["day"] for i in data_reader])
    joao_days_on = set()
    for i in data_reader:
        if i["name"] == "joao":
            joao_days_on.add(i["day"])
    return all_days.difference(joao_days_on)


def write_in_txt(path_to_file, txt_file):
    maria_pedido = maria_mais_pedido(path_to_file)
    arnaldo_pedido = arnaldo_hamburger_count(path_to_file)
    joao_nao_pediu = joao_never_requested(path_to_file)
    joao_nao_veio = joao_days_of(path_to_file)
    text = (
        f"{maria_pedido}\n"
        + f"{arnaldo_pedido}\n"
        + f"{joao_nao_pediu}\n"
        + f"{joao_nao_veio}"
    )
    with open(txt_file, "w") as file:
        file.write(text)


def analyze_log(path_to_file):
    write_in_txt(path_to_file, "data/mkt_campaign.txt")


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
