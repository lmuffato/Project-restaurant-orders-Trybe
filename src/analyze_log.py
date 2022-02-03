from collections import Counter
import csv


path_to_mkt_campaign_file = "data/mkt_campaign.txt"


def read_csv_file(path):
    with open(path) as file:
        all_data = csv.reader(file, delimiter=",", quotechar=" ")
        header, *data = all_data

    return data


def get_most_requested(list, name):
    maria_requests = []

    for item in range(len(list)):
        if list[item][0] == name:
            maria_requests.append(list[item][1])

    most_requested = Counter(maria_requests)

    return max(most_requested, key=most_requested.get)


def update_file(path, row):
    file = open(path, mode="w")
    file.write(row)


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)
    most_requested_from_maria = get_most_requested(data, "maria")

    update_file(path_to_mkt_campaign_file, most_requested_from_maria)
