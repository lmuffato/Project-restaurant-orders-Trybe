import csv

def read_orders_file(path_to_file):
    all_orders = {}
    with open(path_to_file, mode="r") as my_file:
        my_file = csv.reader(my_file)
        for name, order, week_day in my_file:
            if name not in all_orders:
                all_orders[name] = []
            all_orders[name].append((order, week_day))

    return all_orders

def get_most_ordered_by_name(all_orders, person_name):
    person_orders = all_orders[person_name]

    count = {}
    most_ordered = person_orders[0][0]

    for name, day in person_orders:
        if name not in count:
            count[name] = 1
        else:
            count[name] += 1

        if count[name] > count[most_ordered]:
            most_ordered: name

    return most_ordered


def analyze_log(path_to_file):
    all_orders = read_orders_file(path_to_file)
    most_ordered_by_maria = get_most_ordered_by_name(all_orders, "maria")
    print(most_ordered_by_maria)

analyze_log("data/orders_1.csv")