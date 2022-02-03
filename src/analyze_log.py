from collections import Counter
import csv


path_to_mkt_campaign_file = "data/mkt_campaign.txt"
menu = ["pizza", "hamburguer", "coxinha", "misto-quente"]
days = [
    "segunda-feira",
    "terça-feira",
    "sabado",
]


def read_csv_file(path):
    with open(path) as file:
        all_data = csv.reader(file, delimiter=",", quotechar=" ")
        header, *data = all_data

    return data


def get_requests(orders, name):
    requests = []

    for item in range(len(orders)):
        if orders[item][0] == name:
            requests.append(orders[item][1])

    return Counter(requests)


def get_days(orders, name):
    requests = []

    for item in range(len(orders)):
        if orders[item][0] == name:
            requests.append(orders[item][2])

    return requests


def get_days_open(orders):
    requests = []

    for item in range(len(orders)):
        requests.append(orders[item][2])

    return Counter(requests)


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)
    requests_from_maria = get_requests(data, "maria")
    requests_from_arnaldo = get_requests(data, "arnaldo")
    hamburguer_arnaldo = requests_from_arnaldo["hamburguer"]
    requests_from_joao = set(get_requests(data, "joao"))
    not_requested_from_joao = requests_from_joao.symmetric_difference(menu)
    days_joao = set(get_days(data, "joao"))
    off_days_joao = days_joao.symmetric_difference(days)

    most_requested_from_maria = max(
        requests_from_maria, key=requests_from_maria.get
    )

    file = open(path_to_mkt_campaign_file, mode="w")

    print(most_requested_from_maria, file=file)
    print(hamburguer_arnaldo, file=file)
    print(not_requested_from_joao, file=file)
    print(off_days_joao, file=file)

    file.close()
