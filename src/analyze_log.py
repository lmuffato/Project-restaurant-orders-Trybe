import csv


def read_csv(path_to_file):
    data = []
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for name, food, day in reader:
            data.append({
                "name": name,
                "food": food,
                "day": day
            })
    return data


def maria_fav_food(data, customer):
    dicionario = dict()
    for i in data:
        if i["name"] == customer:
            if i["food"] not in dicionario:
                dicionario[i["food"]] = 1
            else:
                dicionario[i["food"]] += 1
    result = max(dicionario, key=dicionario.get)
    return result


def txt(text, txt_file):
    with open(txt, "w") as file:
        file.write(text)


def analyze_log(path_to_file):
    # raise NotImplementedError
    data = read_csv(path_to_file)
    maria_fav = maria_fav_food(data, "maria")

    result = (
        f"{maria_fav}\n"
    )
    txt(result, "data/mkt_campaign.txt")
