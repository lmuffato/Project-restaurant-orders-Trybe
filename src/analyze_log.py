import csv


def analyze_log(path_to_file):
    with open(path_to_file) as csv_file:
        reader_datas = csv.DictReader(csv_file, delimiter=",", quotechar='"')
        return[row for row in reader_datas]
