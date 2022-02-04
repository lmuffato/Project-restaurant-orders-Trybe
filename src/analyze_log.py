import csv

# a funcao list() coloca os dados do arq csv em uma lista
def readFile(path_to_file):
    with open(path_to_file, mode="r") as file:
        dictionary = ["customer", "order", "day"]
        data = csv.reader(file, fieldnames=dictionary)
        answer = list(data)
    return answer


def analyze_log(path_to_file):