import util
from statistics import mode


def get_maria_most_eated_food(df):
    "https://docs.python.org/3.4/library/statistics.html#statistics.mode"
    maria_df = util.filter_row_by_name(df, "maria")
    food_order_list = []
    for row in maria_df:
        food_order_list.append(row[1])
    return mode(food_order_list)


def get_how_many_burguers_arn_has_eated(df):
    arnaldo_df = util.filter_row_by_name(df, 'arnaldo')
    how_many_burgers = 0
    for row in arnaldo_df:
        if row[1] == 'hamburguer':
            how_many_burgers += 1
    return how_many_burgers


def get_joao_not_eated_food(df):
    joao_df = util.filter_row_by_name(df, 'joao')
    full_food_list = util.get_food_list(df)
    joao_food_list = util.get_food_list(joao_df)
    for food in joao_food_list:
        full_food_list.remove(food)
    return full_food_list


def get_ungonne_days_by_joao(df):
    joao_df = util.filter_row_by_name(df, 'joao')
    full_day_list = util.get_day_list(df)
    joao_day_list = util.get_day_list(joao_df)
    for day in joao_day_list:
        full_day_list.remove(day)
    return full_day_list


def analyze_log(path_to_file):
    df = util.read_csv(path_to_file)
    most_eated_food_by_maria = get_maria_most_eated_food(df)
    how_many_burguers_arn_has_eated = get_how_many_burguers_arn_has_eated(df)
    joao_not_eated_food_list = set(get_joao_not_eated_food(df))
    ungonne_days_by_joao = set(get_ungonne_days_by_joao(df))

    msg = f"""{most_eated_food_by_maria}
{how_many_burguers_arn_has_eated}
{joao_not_eated_food_list}
{ungonne_days_by_joao}"""
    print(msg, file=open("./data/mkt_campaign.txt", "w"))
