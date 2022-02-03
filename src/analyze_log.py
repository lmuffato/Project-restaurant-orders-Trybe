import csv

def readFile(path):
    with open(path, mode="r") as file:
        if path.endswith(".csv"):
                reader = csv.reader(file, delimiter=',')
                data = [row for row in reader]
                return data
        else:
            raise ValueError("Arquivo inválido")


def analyze_log(path_to_file):