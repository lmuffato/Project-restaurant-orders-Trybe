import csv
from statistics import mode


def analyze_log(path_to_file):
    foods = ['hamburguer', 'coxinha', 'misto-quente', 'pizza']
    work_days = []
    with open(path_to_file, 'r') as file:
        reader = csv.reader(file)
        my_dict = dict()
        for [nome, comida, dia] in reader:
            if dia not in work_days:
                work_days.append(dia)
            if nome in my_dict.keys():
                my_dict[nome]['foods_eaten'].append(comida)
                my_dict[nome]['days_at_restaurant'].append(dia)
            else:
                my_dict[nome] = {'foods_eaten': [], 'days_at_restaurant': []}
                my_dict[nome]['foods_eaten'].append(comida)
                my_dict[nome]['days_at_restaurant'].append(dia)

    results_dict = {
        1: mode(my_dict['maria']['foods_eaten']),
        2: my_dict['arnaldo']['foods_eaten'].count('hamburguer'),
        3: set([
            food for food in foods
            if food not in my_dict['joao']['foods_eaten']]),
        4: set([
            work_day for work_day in work_days
            if work_day not in my_dict['joao']['days_at_restaurant']])
    }

    with open('./data/mkt_campaign.txt', 'w') as result_file:
        for value in results_dict.values():
            result_file.write(str(value)+'\n')
