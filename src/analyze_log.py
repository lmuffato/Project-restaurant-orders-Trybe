import csv
from collections import Counter


def arnaldo_burguers(csv_file):
    # Quantas vezes arnaldo pediu um hamburguer
    # Ref: https://app.betrybe.com/course/computer-science/introducao-a-python
    # /entrada-e-saida-de-dados/105dc022-72fa-425f-a452-29b3595bb64d/conteudos/9a69f5d2-dd9d-4831-bea0-bb2f7251cc3b/manipulando-arquivos-csv/acbfc282-4ea3-4391-aa85-77f9784efdd2?use_case=side_bar
    count_arnaldo_hamburguers = 0
    for row in csv_file:
        if row["costumer"] == "arnaldo" and row["dish"] == "hamburguer":
            count_arnaldo_hamburguers += 1
    return count_arnaldo_hamburguers


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        if "csv" in path_to_file:
            csv_file = csv.DictReader(
                file, fieldnames=["costumer", "dish", "week_day"]
            )
            maria_favorites = []
            count_arnaldo_hamburguers = arnaldo_burguers(csv_file)
            # https://app.betrybe.com/course/computer-science/introducao-a-python/aprendendo-python/9c4e1d64-303d-492d-82a4-998b2c0218b9/conteudos/217980af-0946-4b04-9cc4-5846af26ec27/tipos-de-dados-embutidos/bea4b2ef-aece-43fe-9d9d-fa7d8c183088?use_case=side_bar
            dishes = set()
            joao_dishes = set()
            week_days = set()
            joao_week_days = set()
            for row in csv_file:
                dishes.add(row["dish"])
                week_days.add(row["week_day"])
                if row["costumer"] == "joao":
                    joao_week_days.add(row["week_day"])
                    joao_dishes.add(row["dish"])
                if row["costumer"] == "maria":
                    maria_favorites.append(row["dish"])
                maria_dishe = Counter(maria_favorites).most_common(1)[0][0]
                dishes_not_ordered_by_joao = dishes - joao_dishes
                joao_week_days_absence = week_days - joao_week_days
                data_string = (
                    f"{maria_dishe}\n"
                    f"{count_arnaldo_hamburguers}\n"
                    f"{dishes_not_ordered_by_joao}\n"
                    f"{joao_week_days_absence}"
                )
                with open("data/mkt_campaign.txt", "w") as txt_file:
                    print(data_string, file=txt_file)
        else:
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'"
            )
