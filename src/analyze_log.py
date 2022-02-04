import csv


def readFile(path_to_file):
    with open(path_to_file, mode="r") as orders:
        data = csv.reader(orders)
        answer = list(data)
    return answer


def analyze_log(path_to_file):