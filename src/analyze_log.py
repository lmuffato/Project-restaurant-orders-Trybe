import csv


def read_file_csv(directory):
    data = []

    with open(directory) as file:
        list_file = csv.reader(file)

        for name, food, week in list_file:
            data.append({"name": name, "food": food, "week": week})
    return data


def analyze_log(path_to_file):
    raise NotImplementedError
    # Parabéns, Mike
