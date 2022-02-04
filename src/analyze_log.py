import pandas as pd


def get_maria_most_eated_food(df):
    maria_df = df[df["Client"] == "maria"][["Comida", "Client"]]
    return maria_df["Comida"].mode()[0]


def get_how_many_burguers_arn_has_eated(df):
    arnaldo_df = df[df["Client"] == "arnaldo"][["Comida", "Client"]]
    return arnaldo_df[arnaldo_df["Comida"] == 'hamburguer'].count()[0]


def get_joao_not_eated_food(df):
    food_list = list(df['Comida'].unique())
    joao_food_list = df[df["Client"] == "joao"]["Comida"].unique()
    for food in joao_food_list:
        food_list.remove(food)
    return food_list


def get_ungonne_days_by_joao(df):
    day_list = list(df["Dia da Semana"].unique())
    joao_day_list = df[df["Client"] == "joao"]["Dia da Semana"].unique()
    for day in joao_day_list:
        day_list.remove(day)
    return day_list


def analyze_log(path_to_file):
    df = pd.read_csv(path_to_file, names=["Client", "Comida", "Dia da Semana"])

    most_eated_food_by_maria = get_maria_most_eated_food(df)
    how_many_burguers_arn_has_eated = get_how_many_burguers_arn_has_eated(df)
    joao_not_eated_food_list = set(get_joao_not_eated_food(df))
    ungonne_days_by_joao = set(get_ungonne_days_by_joao(df))

    msg = f"""{most_eated_food_by_maria}
{how_many_burguers_arn_has_eated}
{joao_not_eated_food_list}
{ungonne_days_by_joao}"""
    print(msg, file=open("./data/mkt_campaign.txt", "w"))


analyze_log('./data/orders_1.csv')
