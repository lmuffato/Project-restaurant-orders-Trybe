import csv
from statistics import mode


def read_csv(path_to_file):
    with open(path_to_file, 'r') as file:
        data = csv.reader(file)
        df = []
        for row in data:
            df.append(row)
    return df


def filter_row_by_name(df, name):
    list_to_return = []
    for row in df:
        if(row[0] == name):
            list_to_return.append(row)
    return list_to_return


def get_food_list(df):
    food_list = []
    for row in df:
        if row[1] not in food_list:
            food_list.append(row[1])
    return food_list


def get_day_list(df):
    day_list = []
    for row in df:
        if row[2] not in day_list:
            day_list.append(row[2])
    return day_list


def get_maria_most_eated_food(df):
    "https://docs.python.org/3.4/library/statistics.html#statistics.mode"
    maria_df = filter_row_by_name(df, "maria")
    food_order_list = []
    for row in maria_df:
        food_order_list.append(row[1])
    return mode(food_order_list)


def get_how_many_burguers_arn_has_eated(df):
    arnaldo_df = filter_row_by_name(df, 'arnaldo')
    how_many_burgers = 0
    for row in arnaldo_df:
        if row[1] == 'hamburguer':
            how_many_burgers += 1
    return how_many_burgers


def get_joao_not_eated_food(df):
    joao_df = filter_row_by_name(df, 'joao')
    full_food_list = get_food_list(df)
    joao_food_list = get_food_list(joao_df)
    for food in joao_food_list:
        full_food_list.remove(food)
    return full_food_list


def get_ungonne_days_by_joao(df):
    joao_df = filter_row_by_name(df, 'joao')
    full_day_list = get_day_list(df)
    joao_day_list = get_day_list(joao_df)
    for day in joao_day_list:
        full_day_list.remove(day)
    return full_day_list


def analyze_log(path_to_file):
    df = read_csv(path_to_file)
    most_eated_food_by_maria = get_maria_most_eated_food(df)
    how_many_burguers_arn_has_eated = get_how_many_burguers_arn_has_eated(df)
    joao_not_eated_food_list = set(get_joao_not_eated_food(df))
    ungonne_days_by_joao = set(get_ungonne_days_by_joao(df))

    msg = f"""{most_eated_food_by_maria}
{how_many_burguers_arn_has_eated}
{joao_not_eated_food_list}
{ungonne_days_by_joao}"""
    print(msg, file=open("./data/mkt_campaign.txt", "w"))


analyze_log("./data/orders_1.csv")
