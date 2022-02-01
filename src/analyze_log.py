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


def days_never_snackBar(tickets):
    list = []
    list_day = []
    for ticket in tickets:
        if ticket["name"] == "joao" and ticket["week"] not in list:
            list.append(ticket["week"])

    for ticket in tickets:
        if ticket["week"] not in list and ticket["week"] not in list_day:
            list_day.append(ticket["week"])
    return set(list_day)


def write_data_file(
    order_by_maria,
    order_by_arnaldo,
    never_ordered_by_joao,
    days_never_snackBar,
):
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{order_by_maria}\n")
        file.write(f"{order_by_arnaldo}\n")
        file.write(f"{never_ordered_by_joao}\n")
        file.write(f"{days_never_snackBar}\n")


def analyze_log(path_to_file):
    result = read_file_csv(path_to_file)
    order_by_maria(result)
    order_by_arnaldo(result)
    never_ordered_by_joao(result)
    days_never_snackBar(result)
    write_data_file(
        order_by_maria(result),
        order_by_arnaldo(result),
        never_ordered_by_joao(result),
        days_never_snackBar(result),
    )
