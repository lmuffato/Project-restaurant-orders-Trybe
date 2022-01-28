import csv


def analyze_log(path_to_file):
    the_dict = {}
    with open(path_to_file) as f:
        csv_readed_file = csv.reader(f)
        seting = set(f.readlines())
        for item in seting:
            name, food, weekday = item.split(',')
            try:
                if the_dict[name] not in the_dict:
                    the_dict[name] = ''
            except KeyError:
                the_dict[name] = ''
        # for position in set(f.readlines()):
        #     name, food, weekday = position.split(',')
        #     people.append(name)
        #     weekdayNFood.append({weekday: food})
    print(the_dict)
    f.close()
    # raise NotImplementedError


analyze_log('../data/orders_1.csv')
