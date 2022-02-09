import csv
import os


def maria_favorite_meal(df):
    unique_meals = list(set([row["pedido"] for row in df]))
    meals = {key: 0 for key in unique_meals}
    for row in df:
        if row["cliente"] == "maria":
            meals[row["pedido"]] += 1
    biggest = ('N/A', 0)
    for key in meals.keys():
        if meals[key] > biggest[1]:
            biggest = (key, meals[key])

    return biggest[0]


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        buffer = csv.DictReader(
            csv_file, fieldnames=["cliente", "pedido", "dia"]
        )
        df = [row for row in buffer]
        # Qual o prato mais pedido por 'maria'?
        maria_favorite = maria_favorite_meal(df)
        # initializing variables
        arnoldo_burguer_count = 0
        joao_dislikes = set([row["pedido"] for row in df])
        joao_missing = set([row["dia"] for row in df])

        for row in df:
            # Quantas vezes 'arnaldo' pediu 'hamburguer'?
            if row["cliente"] == "arnaldo" and row["pedido"] == "hamburguer":
                arnoldo_burguer_count += 1
            if row["cliente"] == "joao":
                # Quais pratos 'joao' nunca pediu?
                joao_dislikes.discard(row["pedido"])
                # Quais dias 'joao' nunca foi na lanchonete?
                joao_missing.discard(row["dia"])

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "..", "data", "mkt_campaign.txt")
    file = open(filename, "w")
    file.write(maria_favorite + "\n")
    file.write(str(arnoldo_burguer_count) + "\n")
    file.write(str(joao_dislikes) + "\n")
    file.write(str(joao_missing))
    file.close()
