import csv


def import_data_csv(path):
    if path.endswith("csv"):
        with open(path, "r") as file:
            return list(csv.reader(file, delimiter=","))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path}'")


def most_requested_dish(data, name):
    count = {}
    answer_number = 1
    answer_name = data[0][1]

    for item in data:
        dish = item[1]
        client = item[0]

        if client == name:
            if dish not in count:
                count[dish] = 1
            else:
                count[dish] += 1

            if count[dish] > answer_number:
                answer_number = count[dish]
                answer_name = dish

    return answer_name


def count_requests(data, name, request):
    count = 0

    for item in data:
        dish = item[1]
        client = item[0]
        if client == name and dish == request:
            count += 1
    return count


def never_requested_dishes(data, name):
    all_dishes = set()
    requested_dishes = set()

    for item in data:
        dish = item[1]
        client = item[0]
        all_dishes.add(dish)
        if client == name:
            requested_dishes.add(dish)

    return all_dishes - requested_dishes


def days_without_going(data, name):
    all_days = set()
    active_days = set()

    for item in data:
        day = item[2]
        client = item[0]
        all_days.add(day)
        if client == name:
            active_days.add(day)

    return all_days - active_days


def analyze_log(path_to_file):
    data = import_data_csv(path_to_file)
    maria_request = most_requested_dish(data, 'maria')
    arnaldo_hamburguer = count_requests(data, 'arnaldo', 'hamburguer')
    joao_never_requested = never_requested_dishes(data, 'joao')
    joao_never_days = days_without_going(data, 'joao')

    with open('data/mkt_campaign.txt', 'w') as file:
        file.writelines(f'{maria_request}\n')
        file.writelines(f'{arnaldo_hamburguer}\n')
        file.writelines(f'{joao_never_requested}\n')
        file.writelines(f'{joao_never_days}\n')
