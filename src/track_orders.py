from src.analyze_log import (
    take_options_less_requested,
    take_the_most_order_requested_by_name,
    get_days_off,
    get_most_crowded_day,
    get_less_crowded_day
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = take_the_most_order_requested_by_name(self.orders, costumer)
        return result

    def get_never_ordered_per_costumer(self, costumer):
        result = take_options_less_requested(self.orders, costumer)
        return result

    def get_days_never_visited_per_costumer(self, costumer):
        result = get_days_off(self.orders, costumer)
        return result

    def get_busiest_day(self):
        result = get_most_crowded_day(self.orders)
        return result

    def get_least_busy_day(self):
        result = get_less_crowded_day(self.orders)
        return result
