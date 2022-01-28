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
    return count


def analyze_log(path_to_file):
    data = reader_file(path_to_file)
    most_requested_by_maria(data)
    arnaldo_requested_hamburguer(data, 'arnaldo')


analyze_log('./data/orders_1.csv')
