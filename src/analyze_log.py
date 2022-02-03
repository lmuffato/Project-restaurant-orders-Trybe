import csv


def analyze_log(path_to_file):
    orders = list()
    dishes = set()
    days = set()
    with open(path_to_file, "r") as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            days.add(row[2])
            dishes.add(row[1])
            orders.append({"costumer": row[0], "order": row[1], "day": row[2]})

        maria_orders = [
            maria["order"] for maria in orders if maria["costumer"] == "maria"
        ]

        maria_max_order = max(maria_orders, key=maria_orders.count)

        arnaldo_hamburger_count = [
            arnaldo["order"]
            for arnaldo in orders
            if arnaldo["costumer"] == "arnaldo"
        ].count("hamburguer")

        joao_never_order = dishes.difference(
            set(
                [
                    joao["order"]
                    for joao in orders
                    if joao["costumer"] == "joao"
                ]
            )
        )

        joao_never_go = days.difference(
            set([joao["day"] for joao in orders if joao["costumer"] == "joao"])
        )
        data = "\n".join(
            [
                str(maria_max_order),
                str(arnaldo_hamburger_count),
                str(joao_never_order),
                str(joao_never_go),
            ]
        )
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(data)
