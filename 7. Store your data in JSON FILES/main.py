from utils import calculate_price, calculate_meal_calories, calculate_combo_calories
from exception import ItemNotFoundException, InfoNotAvailableException
import json

with open('meals.json', 'r') as meals_file:
    meals_data = json.load(meals_file)

with open('combos.json', 'r') as combos_file:
    combos_data = json.load(combos_file)
#examples
meal_id_1 = "meal-1"
meal_price_1, meal_calories_1 = calculate_price(meals_data, combos_data, meal_id_1)
print(f'{meal_id_1} - Price: ${meal_price_1}, Calories: {meal_calories_1} kcal')

combo_id_1 = "combo-3"
combo_price_1, combo_calories_1 = calculate_price(meals_data, combos_data, combo_id_1)
print(f'{combo_id_1} - Price: ${combo_price_1}, Calories: {combo_calories_1} kcal')

combo_ids_2 = ["combo-3", "meal-1"]
combo_price_2, combo_calories_2 = calculate_price(meals_data, combos_data, combo_ids_2)
print(f'{combo_ids_2} - Price: ${combo_price_2}, Calories: {combo_calories_2} kcal')

combo_ids_3 = ["combo-35", "meal-1"]
combo_price_3, combo_calories_3 = calculate_price(meals_data, combos_data, combo_ids_3)
print(f'{combo_ids_3} - Price: ${combo_price_3}, Calories: {combo_calories_3} kcal')
