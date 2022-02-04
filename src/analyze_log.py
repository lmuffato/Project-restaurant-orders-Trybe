from collections import Counter
import csv


def get_orders_log(path_to_file):
    orders_by_customer = {}
    menu = set()
    work_days = set()

    with open(path_to_file) as file:
        orders_log = csv.reader(file)

        for customer, order, week_day in orders_log:
            if customer in orders_by_customer:
                orders_by_customer[customer].append((order, week_day))
            else:
                orders_by_customer[customer] = [(order, week_day)]
            menu.add(order)
            work_days.add(week_day)

    return orders_by_customer, menu, work_days


def analyze_log(path_to_file):
    orders_by_customer, menu, work_days = get_orders_log(path_to_file)

    ordered_by_maria = Counter(orders_by_customer['maria'])
    most_ordered_by_maria = ordered_by_maria.most_common(1)[0][0][0]

    hamburguers_ordered_by_arnaldo = sum(
        1 for food in orders_by_customer['arnaldo'] if food[0] == 'hamburguer'
    )

    ordered_by_joao = set(order[0] for order in orders_by_customer['joao'])
    never_ordered_by_joao = menu.difference(ordered_by_joao)

    joao_attendance = set(order[1] for order in orders_by_customer['joao'])
    joao_absence = work_days.difference(joao_attendance)

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f"{most_ordered_by_maria}\n"
            f"{hamburguers_ordered_by_arnaldo}\n"
            f"{never_ordered_by_joao}\n"
            f"{joao_absence}"
        )
