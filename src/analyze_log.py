import csv


def getDate(path_to_file):
    date = []
    with open(path_to_file) as file:
        beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
        for row in beach_status_reader:
            date.append({"name": row[0], "food": row[1], "day": row[2]})
    return date


def getAnswerMaria(path_to_file):
    date = getDate(path_to_file)
    listResult = []
    for value in date:
        if(value['name'] == 'maria'):
            listResult.append(value['food'])

    return max(listResult, key=listResult.count)


def getAnswerArnaldo(path_to_file):
    date = getDate(path_to_file)
    listResult = []

    for value in date:
        if(value['name'] == 'arnaldo' and value['food'] == 'hamburguer'):
            listResult.append(value['food'])

    return len(listResult)


def getAnswerJoao(path_to_file):
    date = getDate(path_to_file)
    joaoFood = []
    joaoNotFood = []

    for value in date:
        if(value['name'] == 'joao'):
            joaoFood.append(value['food'])

    result = joaoFood[0]

    for value in date:
        if(value['food'] != result):
            joaoNotFood.append(value['food'])

    return set(joaoNotFood)


def getAnswerJoaoTwo(path_to_file):
    date = getDate(path_to_file)
    joaoDay = []
    joaoNotDay = []

    for value in date:
        if(value['name'] == 'joao'):
            joaoDay.append(value['day'])

    result = joaoDay[0]

    for value in date:
        if(value['day'] != result):
            joaoNotDay.append(value['day'])

    return set(joaoNotDay)


def analyze_log(path_to_file):

    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(str(getAnswerMaria(path_to_file)) + '\n')
        file.write(str(getAnswerArnaldo(path_to_file)) + '\n')
        file.write(str(getAnswerJoao(path_to_file)) + '\n')
        file.write(str(getAnswerJoaoTwo(path_to_file)))
