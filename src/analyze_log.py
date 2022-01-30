import csv
from collections import Counter


def arnaldo_data(csv_file):
    count_arnaldo_hamburguers = 0
    for row in csv_file:
        if row['costumer'] == 'arnaldo' and row['dish'] == 'hamburguer':
            count_arnaldo_hamburguers += 1
    return count_arnaldo_hamburguers


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        if('csv' in path_to_file):
            csv_file = csv.DictReader(file, fieldnames=[
                "costumer", "dish", "week_day"])
            maria_dishes = []
            count_arnaldo_hamburguers = arnaldo_data(csv_file)
            dishes = set()
            joao_dishes = set()
            week_days = set()
            joao_week_days = set()
            for row in csv_file:
                dishes.add(row['dish'])
                week_days.add(row['week_day'])
                if row['costumer'] == 'joao':
                    joao_week_days.add(row['week_day'])
                    joao_dishes.add(row['dish'])
                if row['costumer'] == 'maria':
                    maria_dishes.append(row['dish'])
                maria_dishe = Counter(maria_dishes).most_common(1)[0][0]
                dishes_not_ordered_by_joao = dishes - joao_dishes
                joao_week_days_absence = week_days - joao_week_days
                data_string = (
                    f"{maria_dishe}\n"
                    f"{count_arnaldo_hamburguers}\n"
                    f"{dishes_not_ordered_by_joao}\n"
                    f"{joao_week_days_absence}")
                with open('data/mkt_campaign.txt', 'w') as txt_file:
                    print(data_string, file=txt_file)
        else:
            raise FileNotFoundError(
                f"No such file or directory: '{path_to_file}'")


path_to_file = '/home/luiz/Trybe/sd-010-a-restaurant-orders/data/orders_1.csv'
teste = analyze_log(path_to_file)
print(teste)
