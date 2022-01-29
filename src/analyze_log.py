import csv
from collections import Counter


def read_file(path):
    if path.endswith("csv"):
        with open(path, "r") as file:
            data = list(csv.reader(file))
            return data
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def client_info(client, data):
    client_data = list(filter(lambda el: el[0] == client, data))
    return client_data


def all_meals(data):
    meals = list(map(lambda el: el[1], data))
    return meals


def meals_by_client(client, data):
    client_data = client_info(client, data)
    client_meals = list(map(lambda el: el[1], client_data))
    return client_meals


def maria_meals(client, data):
    meals_maria = meals_by_client(client, data)
    most_order = Counter(meals_maria).most_common(1)
    return most_order[0][0]


def arnaldo_meals(client, meal, data):
    meals_arnaldo = meals_by_client(client, data)
    filter_meals = list(filter(lambda el: el == meal, meals_arnaldo))
    meal_count = len(filter_meals)
    return meal_count


def joao_never_requested(client, data):
    meals = set(all_meals(data))
    meals_client = set(meals_by_client(client, data))
    meals_never_order = meals - meals_client
    return meals_never_order


def filter_days(client, data):
    client_data = client_info(client, data)
    client_days = list(map(lambda el: el[2], client_data))
    return client_days


def joao_not_in_restaurant(client, data):
    client_days = set(filter_days(client, data))
    days_week = {"segunda-feira", "terça-feira", "sabado"}
    client_is_not = days_week - client_days
    return client_is_not


def analyze_log(path_to_file):
    data = read_file(path_to_file)
    maria_info = maria_meals("maria", data)
    arnaldo_info = arnaldo_meals("arnaldo", "hamburguer", data)
    joao_info = joao_never_requested("joao", data)
    joao_days = joao_not_in_restaurant("joao", data)
    result = (
        f"{maria_info}\n"
        f"{arnaldo_info}\n"
        f"{joao_info}\n"
        f"{joao_days}\n"
    )
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")
    analyze_log("data/orders_3.csv")
    analyze_log("data/orders_1.txt")
