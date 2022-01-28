from csv import reader


def most_requested_dish_by_maria(data):
    dishes = {}
    for person, dish, _day in data:
        if person == "maria":
            if dish not in dishes:
                dishes[dish] = 1
            else:
                dishes[dish] += 1
    max_value = max(dishes.values())
    max_key = [key for key, value in dishes.items() if value == max_value]
    return max_key[0]


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
            "No such file or directory: 'data/orders_1.txt'"
        )
    file_data = []
    with open(path_to_file, "r") as file:
        file_data = list(reader(file))

    maria_fav_dish = most_requested_dish_by_maria(file_data)
    print(maria_fav_dish)
