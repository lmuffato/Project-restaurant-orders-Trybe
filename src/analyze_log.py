from csv import reader


def maria_most_ordered_dish(data):
    dishes = {}

    for person, dish, _day in data:
        if person == "maria":
            if dish not in dishes:
                dishes[dish] = 1
            else:
                dishes[dish] += 1

    max_value = max(dishes.values())
    result = [key for key, value in dishes.items() if value == max_value]
    return result[0]


def arnaldo_hamburguers_ordered(data):
    count = 0

    for person, dish, _day in data:
        if person == "arnaldo" and dish == "hamburguer":
            count += 1
    return count


def dishes_joao_never_ordered(data):
    dishes = set()
    joao_dishes = set()

    for person, dish, _day in data:
        if dish not in dishes:
            dishes.add(dish)
        if person == "joao" and dish not in joao_dishes:
            joao_dishes.add(dish)

    result = joao_dishes.symmetric_difference(dishes)
    return result


def days_joao_never_came(data):
    weekdays = set()
    days_joao_went = set()

    for person, _dish, day in data:
        if day not in weekdays:
            weekdays.add(day)
        if person == "joao" and day not in days_joao_went:
            days_joao_went.add(day)

    result = days_joao_went.symmetric_difference(weekdays)
    return result


def write_data(customer_data):
    with open("data/mkt_campaign.txt", "w") as file:
        for row in customer_data:
            file.write(f"{row}\n")


def analyze_log(path_to_file):
    data = []

    with open(path_to_file, "r") as file:
        data = list(reader(file))

    maria_fav_dish = maria_most_ordered_dish(data)
    arnaldo_hamburguers = arnaldo_hamburguers_ordered(data)
    dishes_joao_never_asked = dishes_joao_never_ordered(data)
    joao_missing_days = days_joao_never_came(data)

    customer_info = [
        maria_fav_dish,
        arnaldo_hamburguers,
        dishes_joao_never_asked,
        joao_missing_days,
    ]

    write_data(customer_info)
