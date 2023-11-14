from utils import calculate_price, calculate_meal_calories, calculate_combo_calories
from exception import ItemNotFoundException, InfoNotAvailableException

meals = [
    {
        "id": "meal-1",
        "name": "hamburger",
        "calories": 600,
        "price": 5
    },
    {
        "id": "meal-2",
        "name": "cheese burger",
        "calories": 750,
        "price": 7
    },
    {
        "id": "meal-3",
        "name": "veggie burger",
        "calories": 400,
        "price": 6
    },
    {
        "id": "meal-4",
        "name": "vegan burger",
        "calories": 350,
        "price": 6
    },
    {
        "id": "meal-5",
        "name": "sweet potatoes",
        "calories": 230,
        "price": 3
    },
    {
        "id": "meal-6",
        "name": "salad",
        "calories": 15,
        "price": 4
    },
    {
        "id": "meal-7",
        "name": "iced tea",
        "calories": 70,
        "price": 2
    },
    {
        "id": "meal-8",
        "name": "lemonade",
        "calories": 90,
        "price": 2
    }
]

combos = [
    {
        "id": "combo-1",
        "name": "cheesy combo",
        "meals": ["meal-2", "meal-5", "meal-8"],
        "price": 11,
    },
    {
        "id": "combo-2",
        "name": "veggie combo",
        "meals": ["meal-3", "meal-5", "meal-7"],
        "price": 10,
    },
    {
        "id": "combo-3",
        "name": "vegan combo",
        "meals": ["meal-4", "meal-6", "meal-8"],
        "price": 10,
    }
]


meal_id_1 = "meal-1"
meal_price_1, meal_calories_1 = calculate_price(meals, combos, meal_id_1)
print(f'{meal_id_1} - Price: ${meal_price_1}, Calories: {meal_calories_1} kcal')

combo_id_1 = "combo-3"
combo_price_1, combo_calories_1 = calculate_price(meals, combos, combo_id_1)
print(f'{combo_id_1} - Price: ${combo_price_1}, Calories: {combo_calories_1} kcal')

combo_ids_2 = ["combo-3", "meal-1"]
combo_price_2, combo_calories_2 = calculate_price(meals, combos, combo_ids_2)
print(f'{combo_ids_2} - Price: ${combo_price_2}, Calories: {combo_calories_2} kcal')

combo_ids_3 = ["combo-35", "meal-1"]
combo_price_3, combo_calories_3 = calculate_price(meals, combos, combo_ids_3)
print(f'{combo_ids_3} - Price: ${combo_price_3}, Calories: {combo_calories_3} kcal')

