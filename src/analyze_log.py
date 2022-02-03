import csv
from statistics import mode


def analyze_log(path_to_file):
    foods = ['hamburguer', 'coxinha', 'misto-quente', 'pizza']
    work_days = []
    with open(path_to_file, 'r') as file:
        reader = csv.reader(file)
        log_dict = dict()
        for [nome, comida, dia] in reader:
            if dia not in work_days:
                work_days.append(dia)
            if nome in log_dict.keys():
                log_dict[nome]['foods_eaten'].append(comida)
                log_dict[nome]['days_at_restaurant'].append(dia)
            else:
                log_dict[nome] = {'foods_eaten': [], 'days_at_restaurant': []}
                log_dict[nome]['foods_eaten'].append(comida)
                log_dict[nome]['days_at_restaurant'].append(dia)

    results = {
        1: mode(log_dict['maria']['foods_eaten']),
        2: log_dict['arnaldo']['foods_eaten'].count('hamburguer'),
        3: set([
            food for food in foods
            if food not in log_dict['joao']['foods_eaten']]),
        4: set([
            day for day in work_days
            if day not in log_dict['joao']['days_at_restaurant']])
    }

    with open('./data/mkt_campaign.txt', 'w') as result_file:
        for value in results.values():
            result_file.write(str(value)+'\n')
