from typing import Counter


class TrackOrders:
    def __len__(self):
        return len(self.orders)

    def __init__(self):
        self.len = 0
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.len += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        clients_requests = []
        for request in self.orders:
            if request[0] == costumer:
                clients_requests.append(request[1])
        return Counter(clients_requests).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        cardapio = set()
        orders = set()
        for request in self.orders:
            cardapio.add(request[1])
            if request[0] == costumer:
                orders.add(request[1])
        return cardapio - orders

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        never_asked = set()
        for request in self.orders:
            days.add(request[2])
            if request[0] == costumer:
                never_asked.add(request[2])
        return days - never_asked

    def get_busiest_day(self):
        days = []
        for request in self.orders:
            days.append(request[2])
        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []
        for request in self.orders:
            days.append(request[2])
        return Counter(days).most_common()[-1][0]
