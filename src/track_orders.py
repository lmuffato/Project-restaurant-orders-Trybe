from src.util import read_csv, filter_row_by_name, get_day_list, get_food_list
from statistics import mode


class TrackOrders:
    def __init__(self):
        self.df = []

    def __len__(self):
        return len(self.df)

    def add_new_order(self, costumer, order, day):
        self.df.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_df = filter_row_by_name(self.df, costumer)
        food_order_list = []
        for row in costumer_df:
            food_order_list.append(row[1])
        return mode(food_order_list)

    def get_never_ordered_per_costumer(self, costumer):
        costumer_df = filter_row_by_name(self.df, 'joao')
        full_food_list = get_food_list(self.df)
        costumer_food_list = get_food_list(costumer_df)
        for food in costumer_food_list:
            full_food_list.remove(food)
        return set(full_food_list)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_df = filter_row_by_name(self.df, costumer)
        full_day_list = get_day_list(self.df)
        costumer_day_list = get_day_list(costumer_df)
        for day in costumer_day_list:
            full_day_list.remove(day)
        return set(full_day_list)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
