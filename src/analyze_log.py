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


def how_many_times_arnaldo_asked_hamburguer(data):
    hamburguer_count = 0
    for person, dish, _day in data:
        if person == "arnaldo" and dish == "hamburguer":
            hamburguer_count += 1
    return hamburguer_count


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(
            "No such file or directory: 'data/orders_1.txt'"
        )
    file_data = []
    with open(path_to_file, "r") as file:
        file_data = list(reader(file))

    maria_fav_dish = most_requested_dish_by_maria(file_data)
    arnaldo_hamburguer_count = how_many_times_arnaldo_asked_hamburguer(
        file_data
    )
    print(maria_fav_dish)
    print(arnaldo_hamburguer_count)
