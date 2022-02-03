from collections import Counter
import csv


def read_csv_file(path):
    with open(path) as file:
        all_data = csv.reader(file, delimiter=",", quotechar=" ")
        header, *data = all_data

    return data


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)

    maria_requests = []

    for item in range(len(data)):
        if data[item][0] == "maria":
            maria_requests.append(data[item][1])

    most_requested = Counter(maria_requests)

    return max(most_requested, key=most_requested.get)
