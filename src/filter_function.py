from src.file_manager import readWrite
from collections import Counter


def top_dishes(list_data):
    list_maria = []
    for item_list in list_data:
        if item_list[0] == "maria":
            list_maria.append(item_list[1])
            dict_pop = Counter(list_maria)
            result = dict_pop.most_common(1)
    readWrite(result[0][0])


def count_hamburger(list_data):
    list_arnaldo = []
    for item_list in list_data:
        if item_list[0] == "arnaldo":
            list_arnaldo.append(item_list[1])
            dict_pop = Counter(list_arnaldo)
    readWrite(dict_pop["hamburguer"])


def dishes_not_joao(list_data):
    list_joao = set()
    list_all_dishes = set()
    for item_list in list_data:
        list_all_dishes.add(item_list[1])
        if item_list[0] == "joao":
            list_joao.add(item_list[1])
    result = list_all_dishes - list_joao
    readWrite(result)


def joao_is_absent(list_data):
    list_joao = set()
    list_all_days = set()
    for item_list in list_data:
        list_all_days.add(item_list[2])
        if item_list[0] == "joao":
            list_joao.add(item_list[2])
    result = list_all_days - list_joao
    readWrite(result)
