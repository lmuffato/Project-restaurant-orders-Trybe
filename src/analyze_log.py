import csv
from src.track_orders import TrackOrders


def track_restaurant_orders(files):
    with open(files, 'r') as open_file:
        result = list(csv.reader(open_file))
    # track_orders = TrackOrders()
    for name, dish, weekday in result:
        TrackOrders().add_new_order(name, dish, weekday)
    return TrackOrders()


def saving_data(data_to_save):
    lines = [
        data_to_save.get_most_ordered_dish_per_customer("maria"),
        data_to_save.get_order_frequency_per_customer("arnaldo", "hamburguer"),
        data_to_save.get_never_ordered_per_customer("joao"),
        data_to_save.get_days_never_visited_per_customer("joao")
    ]
    try:
        with open('data/mkt_campaign.txt', 'w') as file:
            for line in lines:
                file.write("{}\n".format(line))
    except FileNotFoundError:
        print('Problema com o arquivo')


def analyze_log(path_to_file):
    if not path_to_file.endswith('csv'):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    result = track_restaurant_orders(path_to_file)
    saving_data(result)
