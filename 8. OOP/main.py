from utils import calculate_price, calculate_meal_calories, calculate_combo_calories
from order import Order
from exception import ItemNotFoundException, InfoNotAvailableException
import json

with open("meals.json", "r") as meals_file:
    meals_data = json.load(meals_file)

with open("combos.json", "r") as combos_file:
    combos_data = json.load(combos_file)

my_order1 = Order()
# Add items to the order
my_order1.add_item("combo-1")
my_order1.add_item("meal-1")
my_order1.add_item("combo-3")
my_order1.print_receipt(meals_data["meals"], combos_data["combos"])

my_order2 = Order()
# Add items to the order
my_order2.add_item("combo-1")
my_order2.add_item("meal-1")
my_order2.print_receipt(meals_data["meals"], combos_data["combos"])

my_order3 = Order()
# Add items to the order
my_order3.add_item("meal-1")
my_order3.add_item("meal-3")
my_order3.print_receipt(meals_data["meals"], combos_data["combos"])
