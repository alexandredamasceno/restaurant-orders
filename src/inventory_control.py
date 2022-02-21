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

    def get_available_dishes(self):
        orders_available = set()
        for order, ingredients in self.INGREDIENTS.items():
            orders_available.add(order)
            for item in ingredients:
                if self.MINIMUM_INVENTORY[item] < 1:
                    orders_available.remove(order)
                    break

        return orders_available

    def verify_inventory(self, order):
        current_ingredients = self.INGREDIENTS[order]
        for item in current_ingredients:
            if self.MINIMUM_INVENTORY[item] < 1:
                return False

    def add_new_order(self, costumer, order, day):
        data = [costumer, order, day]
        if self.verify_inventory(order) is False:
            return False
        self.orders.append(data)
        update_inventory(
            data, self.INGREDIENTS, self.total_to_buy
        )

    def get_quantities_to_buy(self):
        return self.total_to_buy


order = InventoryControl()
print(order.add_new_order("Alexandre", "coxinha", "terça-feira"))
# print(order.add_new_order("Alexandre", "pizza", "segunda-feira"))
# count = 1
# while count <= 50:
#     order.add_new_order("jorge", "hamburguer", "terça-feira")
#     order.add_new_order("maria", "pizza", "terça-feira")
#     count += 1
# hamburguer_pizza = order.add_new_order(
#     "jorge", "hamburguer", "terça-feira"
# )
print(order.get_quantities_to_buy())
print(order.get_available_dishes())
print(order.MINIMUM_INVENTORY)
