from csv import reader

def maria_most_ordered_dish(data):
    print(data)


def arnaldo_hamburguers_ordered(data):
    print(data)


def dishes_joao_never_ordered(data):
    print(data)


def days_joao_never_came(data):
    print(data)


def write_data(customer_data):
    with open("data/mkt_campaign.txt", "w") as file:

def analyze_log(path_to_file):
    data = []

    with open(path_to_file, "r") as file:
        data = list(reader(file))
    
    maria_fav_dish = maria_most_ordered_dish(data)
    arnaldo_hamburguers = arnaldo_hamburguers_ordered(data)
    dishes_joao_never_asked = dishes_joao_never_ordered(data)
    joao_missing_days = days_joao_never_came(data)

    customer_info = [
        maria_fav_dish,
        arnaldo_hamburguers,
        dishes_joao_never_asked,
        joao_missing_days,
    ]
    
    write_data(customer_info)
