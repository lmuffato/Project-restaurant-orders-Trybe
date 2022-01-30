import csv


def read(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        return [{
                  'client': row[0],
                  'order': row[1],
                  'day': row[2],
                } for row in reader]

def analyze_log(path_to_file):
    raise NotImplementedError

