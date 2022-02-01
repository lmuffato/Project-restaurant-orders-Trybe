from csv import reader

def maria_most_ordered_dish(data):
    dishes = {}

    for person, dish, _day in data:
        if person == "maria":
            if dish not in dishes:
                dishes[dish] = 1
            else:
                dishes[dish] += 1
    
    result = [key for key, value in dishes.items() if value == max(dishes.values())]
    return result[0]

    ## Ref.: https://pt.stackoverflow.com/questions/475306/como-acessar-a-chave-pelo-valor-em-dicion%C3%A1rio-python


def arnaldo_hamburguers_ordered(data):
    print(data)


def dishes_joao_never_ordered(data):
    print(data)


def days_joao_never_came(data):
    print(data)


def write_data(customer_data):
    with open("data/mkt_campaign.txt", "w") as file:
        for row in customer_data:
            file.write(f"{row}\n")


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
