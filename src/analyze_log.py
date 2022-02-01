import csv
from statistics import mode


def most_eaten_food(dict_list, customer):
    dishes = []
    for lis in dict_list:
        if lis[0] == customer:
            dishes.append(lis[1])
    return mode(dishes)


def how_many_food(dict_list, food, customer):
    count = 0
    for lis in dict_list:
        if lis[0] == customer and lis[1] == food:
            count += 1
    return count


def customer_never_interacted(dict_list, customer, ind):
    all_interactions = set()
    customer_interactions = set()
    for lis in dict_list:
        all_interactions.add(lis[ind])
        if lis[0] == customer:
            customer_interactions.add(lis[ind])
    return all_interactions - customer_interactions


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
            joao_never_ate = customer_never_interacted(dict_list, 'joao', 1)
            joao_never_been = customer_never_interacted(dict_list, 'joao', 2)
            output.write(f"{maria_most_eaten}\n{arnaldo_count}\n")
            output.write(f"{joao_never_ate}\n{joao_never_been}")
            print(customer_never_interacted(dict_list, 'joao', 2))
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
