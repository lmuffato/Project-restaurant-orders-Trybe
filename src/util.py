import csv


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
