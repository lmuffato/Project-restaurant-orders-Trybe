import csv

# Import CSV to list. Ref:
# https://stackoverflow.com/questions/24662571/python-import-csv-to-list


def import_data(path_to_file):
    if path_to_file.endswith("csv"):
        with open(path_to_file) as file:
            csv_file = csv.reader(file, delimiter=",")
            return list(csv_file)
    else:
        raise ValueError("Arquivo inválido")


# print(import_data("data/orders_1.csv"))


def analyze_log(path_to_file):
    #
    raise NotImplementedError
