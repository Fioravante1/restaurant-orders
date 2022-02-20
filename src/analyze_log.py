import csv
from typing import Counter
import os


def reader(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=",")
        return [val for val in reader]


def most_requested_dish(client, path):
    requests = reader(path)
    clients_requests = []
    for request in requests:
        if request[0] == client:
            clients_requests.append(request[1])
    return Counter(clients_requests).most_common(1)[0][0]


def times_ordered_hamburger(client, path):
    requests = reader(path)
    count = 0
    for request in requests:
        if request[0] == client and request[1] == "hamburguer":
            count += 1
    return count


def dishes_never_ordered(client, path):
    requests = reader(path)
    cardapio = set()
    orders = set()
    for request in requests:
        cardapio.add(request[1])
        if request[0] == client:
            orders.add(request[1])
    return cardapio - orders


def days_never_asked(client, path):
    requests = reader(path)
    days = set()
    never_asked = set()
    for request in requests:
        days.add(request[2])
        if request[0] == client:
            never_asked.add(request[2])
    return days - never_asked


def analyze_log(path_to_file):
    maria_most_requested_dish = most_requested_dish("maria", path_to_file)
    arnaldo_ordered_hamburger = times_ordered_hamburger(
        "arnaldo", path_to_file
    )
    joao_never_ordered = dishes_never_ordered("joao", path_to_file)
    joao_never_days = days_never_asked("joao", path_to_file)

    if not path_to_file.endswith(".csv") or not os.path.exists(path_to_file):
        raise FileNotFoundError("File not found")
    else:
        file = open("data/mkt_campaign.txt", "w")

        file.writelines(
            "{}\n{}\n{}\n{}\n".format(
                maria_most_requested_dish,
                arnaldo_ordered_hamburger,
                joao_never_ordered,
                joao_never_days,
            ),
        )
