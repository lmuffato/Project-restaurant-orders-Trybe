import csv


def get_favorite_order(path_to_file, person):
    with open(path_to_file) as csvfile:
        data = csv.reader(csvfile)
        personsOrders = list()
        for personName, order, date in data:
            if personName == person:
                personsOrders.append(order)
        return max(personsOrders, key=personsOrders.count)


def analyze_log(path_to_file):
    mariasFavorite = get_favorite_order(path_to_file, 'maria')
    final_file = open('data/mkt_campaign.txt', 'w')
    final_file.write(mariasFavorite)
