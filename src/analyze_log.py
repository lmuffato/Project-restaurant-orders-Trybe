import csv


def reader_file(path):
    if (path.endswith('.csv')):
        with open(path, mode='r') as file:
            data = list(csv.reader(file))
            return data
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def most_requested_by_maria(data):
    foods_quant = {}
    for name, food, day in data:
        if (name == 'maria'):
            if (food not in foods_quant):
                foods_quant[food] = 1
            else:
                foods_quant[food] += 1
    # https://thispointer.com/python-how-to-get-all-keys-with-maximum-value-in-a-dictionary/
    itemMaxValue = max(foods_quant.items(), key=lambda x: x[1])
    return itemMaxValue[0]


def arnaldo_requested_hamburguer(data, costumer):
    count = 0
    for name, food, day in data:
        if (name == costumer and food == 'hamburguer'):
            count += 1
    return str(count)


def joao_never_request(data, costumer):
    foods = []
    foods_requested = []
    for name, food, day in data:
        if (food not in foods):
            foods.append(food)
        if (name == costumer):
            foods_requested.append(food)
    # https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
    output = set(foods) - set(foods_requested)
    return output


def days_joao_not_go(data, costumer):
    days = []
    days_go = []
    for name, food, day in data:
        if (day not in days):
            days.append(day)
        if (name == costumer):
            days_go.append(day)
    output = set(days) - set(days_go)
    return output


def analyze_log(path_to_file):
    data = reader_file(path_to_file)
    maria_mr = most_requested_by_maria(data)
    arnaldo_rh = arnaldo_requested_hamburguer(data, 'arnaldo')
    joao_nr = joao_never_request(data, 'joao')
    joao_ng = days_joao_not_go(data, 'joao')
    results = [maria_mr, arnaldo_rh, joao_nr, joao_ng]
    with open("data/mkt_campaign.txt", mode='w') as file:
        for item in results:
            file.write(f"{item}\n")


analyze_log('./data/orders_1.csv')
