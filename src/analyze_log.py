import csv


def read_csv(path_to_file):
    data = []
    with open(path_to_file) as file:
        reader = csv.reader(file)
        for name, food, day in reader:
            data.append({
                "name": name,
                "food": food,
                "day": day
            })
    return data


def analyze_log(path_to_file):
    raise NotImplementedError
