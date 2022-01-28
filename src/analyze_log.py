import csv


def get_favorite_order(data, person):
    personsOrders = list()
    for personName, order, date in data:
        if personName == person:
            personsOrders.append(order)
    return max(personsOrders, key=personsOrders.count)


def count_orders_by_person(data, person, order):
    personsOrders = list()
    for personName, personOrder, date in data:
        if personName == person:
            personsOrders.append(personOrder)
    return personsOrders.count(order)


def never_ordered_by_person(data, person):
    personsOrders = set()
    menu = set()
    neverOrdered = set()
    for personName, personOrder, date in data:
        if personName == person:
            personsOrders.add(personOrder)
        menu.add(personOrder)
    for ordered in menu:
        if ordered not in personsOrders:
            neverOrdered.add(ordered)
    return neverOrdered


def get_days_not_frequented_by_person(data, person):
    frequented_days = set()
    schedule = set()
    not_frequented = set()
    for personName, personOrder, date in data:
        if personName == person:
            frequented_days.add(date)
        schedule.add(date)
    for day in schedule:
        if day not in frequented_days:
            not_frequented.add(day)
    return not_frequented


def analyze_log(path_to_file):
    mariasFavorite = get_favorite_order(
        csv.reader(open(path_to_file)),
        'maria'
    )
    arnaldoHamburgerCount = count_orders_by_person(
        csv.reader(open(path_to_file)),
        'arnaldo',
        'hamburguer',
    )
    neverOrderedByJoao = never_ordered_by_person(
        csv.reader(open(path_to_file)),
        'joao'
    )
    daysNotFrequentedByJoao = get_days_not_frequented_by_person(
        csv.reader(open(path_to_file)),
        'joao'
    )
    final_file = open('data/mkt_campaign.txt', 'w')
    final_file.write(mariasFavorite)
    final_file.write(f"\n{arnaldoHamburgerCount}")
    final_file.write(f"\n{neverOrderedByJoao}")
    final_file.write(f"\n{daysNotFrequentedByJoao}")
