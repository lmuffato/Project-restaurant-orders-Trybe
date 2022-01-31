import csv


def read_file_csv(directory):
    data = []

    with open(directory) as file:
        list_file = csv.reader(file)

        for name, food, week in list_file:
            data.append({"name": name, "food": food, "week": week})
    return data


def order_by_maria(tickets):
    most_common_requests = tickets[0]["food"]
    frequency = {}

    for ticket in tickets:
        if ticket["name"] == "maria":
            if ticket["food"] not in frequency:
                frequency[ticket["food"]] = 1
            else:
                frequency[ticket["food"]] += 1
            if frequency[ticket["food"]] > frequency[most_common_requests]:
                most_common_requests = ticket["food"]
    return most_common_requests


def order_by_arnaldo(tickets):
    value_initial = 0
    for ticket in tickets:
        if ticket["name"] == "arnaldo" and ticket["food"] == "hamburguer":
            value_initial = +1
    return value_initial


def never_ordered_by_joao(tickets):
    list = []
    not_ticket_food = []
    for ticket in tickets:
        if ticket["name"] == "joao" and ticket["food"] not in list:
            list.append(ticket["food"])

    for ticket in tickets:
        if (
            ticket["food"] not in list
            and ticket["food"] not in not_ticket_food
        ):
            not_ticket_food.append(ticket["food"])
    return set(not_ticket_food)


def analyze_log(path_to_file):
    raise NotImplementedError
    # Parabéns, Mike
