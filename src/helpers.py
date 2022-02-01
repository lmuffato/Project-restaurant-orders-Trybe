from csv import reader


#função para ler o arquivo csv
def read_csv(path):
    array = []
    with open(path, "r") as file:
        add_array = reader(file, delimiter=",", quotechar='"')
        for row in add_array:
            customer, food, date = row
            array.append(
                {'customer': customer, 'food': food, 'date': date}
            )
    return array

