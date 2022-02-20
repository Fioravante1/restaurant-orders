from reprlib import recursive_repr
from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.ingredients_sold = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }
        self.inventory_cop = self.MINIMUM_INVENTORY.copy()

# requisito feito com a ajuda do repositorio de Matheus Scheiner

    def add_new_order(self, costumer, order, day):
        TrackOrders().add_new_order(costumer, order, day)
        if self.check_inventory(order):
            for ingredient in self.INGREDIENTS[order]:
                self.inventory_cop[ingredient] -= 1
                self.ingredients_sold[ingredient] += 1
        return False

    def get_quantities_to_buy(self):
        return self.ingredients_sold

    def get_available_dishes(self):
        return {i for i in self.INGREDIENTS if self.check_inventory(i)}

    def check_inventory(self, order):
        return all(self.inventory_cop[i] != 0 for i in self.INGREDIENTS[order])
