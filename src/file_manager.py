import csv


def readFile(path_to_file):
    list_lines = []
    with open(path_to_file, encoding="utf-8") as file:
        data_log = csv.reader(file, delimiter=",")
        for line in data_log:
            list_lines.append(line)
        return list_lines


def readWrite(list_data):
    path_to_file = "./data/mkt_campaign.txt"
    with open(path_to_file, "a") as file:
        file.write(f"{list_data}\n")
