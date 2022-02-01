import csv
from statistics import mode


def most_eaten_food(dict_list, custumer):
    dishes = []
    for lis in dict_list:
        if lis[0] == custumer:
            dishes.append(lis[1])
    return mode(dishes)


def how_many_food(dict_list, food, custumer):
    count = 0
    for lis in dict_list:
        if lis[0] == custumer and lis[1] == food:
            count += 1
    return count


def analyze_log(path_to_file):
    output = open("./data/mkt_campaign.txt", mode="w")
    if path_to_file.endswith('.csv'):
        with open(path_to_file) as file:
            dict_obj = csv.reader(file, delimiter=',', quotechar='|')
            dict_list = []
            for lists in dict_obj:
                dict_list.append(lists)
            maria_most_eaten = most_eaten_food(dict_list, 'maria')
            arnaldo_count = how_many_food(dict_list, 'hamburguer', 'arnaldo')
            output.write(f"{maria_most_eaten}\n{arnaldo_count}\n")
    else:
        raise FileNotFoundError('arquivo nao encontrado')


analyze_log("./data/orders_1.csv")
