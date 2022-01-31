import csv
from collections import Counter

# https://stackoverflow.com/questions/17039539/replace-fieldnames-when-using-dictreader
# inserir chaves em dict


def file_reader(path_to_file):
    with open(path_to_file, 'r') as file:
        chaves = ["customer_name", "order", "day"]
        dict_data = csv.DictReader(file, fieldnames = (chaves))
        data_file = [data for data in dict_data]
        return data_file


def custumer_info(data, name):
    cus_info = [dict for dict in data if dict['customer_name'] == name]
    return cus_info


# Requisito realizado com ajuda de Malíria Cegalla - turma 10A

# https://www.datacamp.com/community/tutorials/python-count?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-392016246653:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1001686&gclid=Cj0KCQiAi9mPBhCJARIsAHchl1zuUMoBqRf8zFrEzjd-1oxvKx3GLguZEQu3gbNslxyOB5KZbymP6ooaAj_hEALw_wcB

# primeiro [0] tira da lista - segundo [0] tira da tupla

def most_ordered_food(data):
    all_orders = [single_dict['order'] for single_dict in data]
    count = Counter(all_orders)
    most_ordered = count.most_common(1)[0][0]
    return most_ordered


# https://www.w3schools.com/python/ref_dictionary_get.asp

def total_order_food(data, food):
    orders = [dict['order'] for dict in data if dict['order'] == food]
    count = Counter(orders)
    result = count.get(food)
    return result


def food_never_ordered(data, customer_infos):
    all_orders = [single_dict['order'] for single_dict in data]
    customer_orders = [single_dict['order'] for single_dict in customer_infos]
    all_orders_set = set(all_orders)
    customer_orders_set = set(customer_orders)
    return all_orders_set.difference(customer_orders_set)


def days_never_been_at(data, customer_data):
    days_open_restaurant = [single_dict['day'] for single_dict in data]
    custumer_days_been = [single_dict['day'] for single_dict in customer_data]
    days_open_restaurant_set = set(days_open_restaurant)
    custumer_days_been_set = set(custumer_days_been)
    return days_open_restaurant_set.difference(custumer_days_been_set)


def analyze_log(path_to_file):
    data = file_reader(path_to_file)
    arr = []

    maria_infos = custumer_info(data, "maria")
    m_most_ordered_food = most_ordered_food(maria_infos)
    arr.append(m_most_ordered_food)

    arnaldo_infos = custumer_info(data, "arnaldo")
    arnaldo_product_total_order_food = total_order_food(
        arnaldo_infos, "hamburguer"
        )
    arr.append(arnaldo_product_total_order_food)

    joao_infos = custumer_info(data, "joao")
    joao_food_never_ordered = food_never_ordered(data, joao_infos)
    arr.append(joao_food_never_ordered)
    joao_days_never_been_at = days_never_been_at(data, joao_infos)
    arr.append(joao_days_never_been_at)

    with open('data/mkt_campaign.txt', 'w') as file:
        for item in arr:
            file.write(str(item) + '\n')
