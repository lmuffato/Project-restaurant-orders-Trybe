from .helpers import read_csv, order_food, counter_order
from .helpers import food_never_ordered, write_data, never_date


def analyze_log(path_to_file):
    orders_history = read_csv(path_to_file)
    most_order = order_food('maria', orders_history)
    count_ordered = counter_order('arnaldo', 'hamburguer', orders_history)
    meal_not_ordered = food_never_ordered('joao', orders_history)
    no_order_day = never_date('joao', orders_history)
    file = f"{most_order}\n{count_ordered}\n{meal_not_ordered}\n{no_order_day}"
    write_data(file)
