import pandas as pd
import os


def analyze_log(path_to_file):
    df: pd.DataFrame = pd.read_csv(
        path_to_file, header=None, names=["cliente", "pedido", "dia"]
    )

    # Qual o prato mais pedido por 'maria'?
    maria_favorite = (
        df.loc[df["cliente"] == "maria"].value_counts().idxmax()[1]
    )
    arnoldo_burguer_count = 0
    joao_dislikes = set(df["pedido"])
    joao_missing = set(df["dia"])

    for row in df.values:
        # Quantas vezes 'arnaldo' pediu 'hamburguer'?
        if row[0] == "arnaldo" and row[1] == "hamburguer":
            arnoldo_burguer_count += 1
        if row[0] == "joao":
            # Quais pratos 'joao' nunca pediu?
            joao_dislikes.discard(row[1])
            # Quais dias 'joao' nunca foi na lanchonete?
            joao_missing.discard(row[2])

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, "..", "data", "mkt_campaign.txt")
    file = open(filename, "w")
    file.write(maria_favorite + "\n")
    file.write(str(arnoldo_burguer_count) + "\n")
    file.write(str(joao_dislikes) + "\n")
    file.write(str(joao_missing))
    file.close()


dir = os.path.dirname(__file__)
filename = os.path.join(dir, "..", "data", "orders_1.csv")
analyze_log(filename)
