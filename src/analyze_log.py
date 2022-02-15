import csv


def get_orders(list, name):
    orders = {}
    for item in list:
        if item["maria"] == name:
            if item["hamburguer"] not in orders:
                orders[item["hamburguer"]] = 1
            else:
                orders[item["hamburguer"]] += 1
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


def get_days_off_joao(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            result = csv.DictReader(file)
            days_week = [
                "segunda-feira",
                "terça-feira",
                "sabado",
            ]
            days_joao = [
                item["terça-feira"]
                for item in result
                if item["maria"] == "joao"
            ]
            days_off = set()
            for item in days_week:
                if not days_joao.count(item):
                    days_off.add(item)

            return days_off
    except FileNotFoundError:
        expect_text = f"No such file or directory: '{path_to_file}'"
        raise FileNotFoundError(expect_text)


def take_maria(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            result = csv.DictReader(file)
            orders = get_orders(result, "maria")
            return get_bigger(orders)
    except FileNotFoundError:
        expect_text = f"No such file or directory: '{path_to_file}'"
        raise FileNotFoundError(expect_text)


def take_arnaldo(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            result = csv.DictReader(file)
            orders = get_orders(result, "arnaldo")
            return orders["hamburguer"]
    except FileNotFoundError:
        expect_text = f"No such file or directory: '{path_to_file}'"
        raise FileNotFoundError(expect_text)


def take_joao(path_to_file):
    try:
        with open(path_to_file, "r") as file:
            options = {
                "hamburguer": 0,
                "pizza": 0,
                "coxinha": 0,
                "misto-quente": 0,
            }
            for item in csv.DictReader(file):
                if item["maria"] == "joao" and item["hamburguer"] in options:
                    options[item["hamburguer"]] += 1
            return get_dont_pick(options)
    except FileNotFoundError:
        expect_text = f"No such file or directory: '{path_to_file}'"
        raise FileNotFoundError(expect_text)


def analyze_log(path_to_file):
    days_off_joao = get_days_off_joao(path_to_file)
    maria = take_maria(path_to_file)
    arnaldo = take_arnaldo(path_to_file)
    joao = take_joao(path_to_file)
    lista = [
        f"{str(maria)}\n",
        f"{str(arnaldo)}\n",
        f"{str(joao)}\n",
        f"{str(days_off_joao)}",
    ]
    with open("data/mkt_campaign.txt", "w") as file:
        file.writelines(lista)
