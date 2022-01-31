import csv


def analyze_log(path_to_file):
    log_dict = get_logs(path_to_file)
    maria_most_ordered = get_maria_most_ordered(log_dict)
    arnaldo_hamburger_orders = get_arnaldo_hamburger_orders(log_dict)
    (joao_not_ordered, days_not_visited) = get_joao_insights(log_dict)

    with open("data/mkt_campaign.txt", mode="w") as file:
        LINES = [
            f"{maria_most_ordered}\n",
            f"{arnaldo_hamburger_orders}\n",
            f"{joao_not_ordered}\n",
            f"{days_not_visited}\n"
        ]
        file.writelines(LINES)


def get_logs(path):
    list = []
    field_names = ['cliente', 'pedido', 'dia']
    with open(path) as file:
        content = csv.DictReader(
            file, delimiter=",",
            quotechar='"',
            fieldnames=field_names
        )
        for row in content:
            list.append(row)
    return list


def get_maria_most_ordered(log):
    count = {}
    most_frequent = log[0]['pedido']

    for item in log:
        if item['pedido'] not in count:
            count[item['pedido']] = 1
        else:
            count[item['pedido']] += 1

        if count[item['pedido']] > count[most_frequent]:
            most_frequent = item['pedido']

    return most_frequent


def get_arnaldo_hamburger_orders(log):
    count = 0
    for item in log:
        if item['cliente'] == 'arnaldo' and item['pedido'] == 'hamburguer':
            count += 1
    return count


def get_joao_insights(log):
    opt = set(row['pedido'] for row in log)
    ordered = set()

    days = set(row['dia'] for row in log)
    days_visited = set()

    for item in log:
        if item['cliente'] == 'joao':
            ordered.add(item['pedido'])
            days_visited.add(item['dia'])

    return (opt.difference(ordered), days.difference(days_visited))
