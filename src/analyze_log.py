import csv


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        read = csv.reader(file)
        data = list(read)
    return data
