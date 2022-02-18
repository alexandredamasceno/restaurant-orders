from src.analyze_log import (
    update_inventory,
)


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []
        self.total_to_buy = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, costumer, order, day):
        data = [costumer, order, day]
        self.orders.append(data)
        update_inventory(
            data, self.MINIMUM_INVENTORY, self.INGREDIENTS, self.total_to_buy
        )

    def get_quantities_to_buy(self):
        return self.total_to_buy


# order = InventoryControl()
# order.add_new_order("Alexandre", "hamburguer", "segunda-feira")
# print(order.get_quantities_to_buy())
