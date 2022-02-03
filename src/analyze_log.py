import csv


def read_csv_file(path):
    with open(path) as file:
        all_data = csv.reader(file, delimiter=",", quotechar=" ")
        header, *data = all_data

    return data


def analyze_log(path_to_file):
    raise NotImplementedError
