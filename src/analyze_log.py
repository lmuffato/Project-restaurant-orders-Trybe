import csv


def read_csv_file(path_to_file):
    with open(path_to_file) as file:
        dict_keys = ["customer", "order", "day"]

        reader = csv.DictReader(file, fieldnames=dict_keys)
        data = list(reader)
    return data


def filter_order_by_customer(data, customer):
    filtered_data = [item for item in data if item["customer"] == customer]

    return filtered_data


def analyze_log(path_to_file):

    data_order = read_csv_file(path_to_file)

    get_maria_order = filter_order_by_customer(data_order, "maria")

    return data_order

# Starting the project
