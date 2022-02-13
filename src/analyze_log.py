import csv


# Qual o prato mais pedido por 'maria'?
def max_order_by_customer(customer, data):
    result = []

    for row in data:
        if row[0] == customer:
            result.append(row[1])
    return max(result, key=result.count)


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
def count_hamburgers(customer, data):
    count = 0

    for row in data:
        if row[0] == customer and row[1] == "hamburguer":
            count += 1
    return count


# Quais pratos 'joao' nunca pediu?
def customer_never_ordered(customer, data):
    all_foods = [row[1] for row in data]
    foods_ordered_by_customer = []

    for row in data:
        if row[0] == customer:
            foods_ordered_by_customer.append(row[1])
    return set(all_foods) - set(foods_ordered_by_customer)


# Quais dias 'joao' nunca foi na lanchonete?
def days_customer_never_ordered(name, data):
    days_customer_ordered = []
    all_days = [row[2] for row in data]

    for row in data:
        if row[0] == name:
            days_customer_ordered.append(row[2])
    return set(all_days) - set(days_customer_ordered)


def analyze_log(path_to_file):

    with open(path_to_file) as file:
        reader = csv.reader(file, delimiter=",")
        data = [row for row in reader]

    ordered_by_maria = max_order_by_customer("maria", data)
    count_hamburgers_by_arnaldo = count_hamburgers("arnaldo", data)
    foods_joao_never_ordered = customer_never_ordered("joao", data)
    days_joao_never_ordered = days_customer_never_ordered("joao", data)

    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(
            [
                f"{ordered_by_maria}\n",
                f"{count_hamburgers_by_arnaldo}\n",
                f"{foods_joao_never_ordered}\n",
                f"{days_joao_never_ordered}\n",
            ]
        )
