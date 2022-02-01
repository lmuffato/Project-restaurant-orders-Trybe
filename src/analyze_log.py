import csv


def read_csv_file(path_to_file):
    with open(path_to_file) as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def analyze_log(path_to_file):

    data_order = read_csv_file(path_to_file)

    return data_order

# Starting the project
