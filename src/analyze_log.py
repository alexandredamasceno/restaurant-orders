import csv


def read_file(path):
    try:
        with open(path, "r") as file:
            result = csv.reader(file, delimiter=",")
            data = [item for item in result]
            return data
    except FileNotFoundError:
        expect_text = f"No such file or directory: '{path}'"
        raise FileNotFoundError(expect_text)


def get_orders(list, name):
    orders = {}
    for item in list:
        if item[0] == name:
            if item[1] not in orders:
                orders[item[1]] = 1
            else:
                orders[item[1]] += 1
    return orders


def get_bigger(dict):
    bigger = max(dict.values())
    for key, value in dict.items():
        if value == bigger:
            return key


def get_dont_pick(dict):
    num = 0
    keys = set()
    for key, value in dict.items():
        if value == num:
            keys.add(key)
    return keys


def get_days_off(file, name):
    days_week = [
        "segunda-feira",
        "terça-feira",
        "sabado",
    ]
    days_on = [
        item[2]
        for item in file
        if item[0] == name
    ]
    days_off = set()
    for item in days_week:
        if not days_on.count(item):
            days_off.add(item)

    return days_off

def take_the_most_order_requested_by_name(file, name):
    orders = get_orders(file, name)
    return get_bigger(orders)


def take_the_less_order(file, name):
    orders = get_orders(file, name)
    minimum = min(orders.values())
    for key, value in orders.items():
        if value == minimum:
            return value


def take_options_less_requested(file, name):
    options = {
        "hamburguer": 0,
        "pizza": 0,
        "coxinha": 0,
        "misto-quente": 0,
    }
    for item in file:
        if item[0] == name and item[1] in options:
            options[item[1]] += 1
    return get_dont_pick(options)


def analyze_log(path_to_file):
    file = read_file(path_to_file)
    days_off_joao = get_days_off(file, "joao")
    maria = take_the_most_order_requested_by_name(file, "maria")
    arnaldo = take_the_less_order(file, "arnaldo")
    joao = take_options_less_requested(file, "joao")
    lista = [
        f"{str(maria)}\n",
        f"{str(arnaldo)}\n",
        f"{str(joao)}\n",
        f"{str(days_off_joao)}",
    ]
    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(lista)


analyze_log("data/orders_1.csv")