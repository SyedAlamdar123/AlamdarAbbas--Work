meals = [
    {"id": "meal-1", "name": "hamburger", "calories": 600, "price": 5},
    {"id": "meal-2", "name": "cheese burger", "calories": 750, "price": 7},
    {"id": "meal-3", "name": "veggie burger", "calories": 400, "price": 6},
    {"id": "meal-4", "name": "vegan burger", "calories": 350, "price": 6},
    {"id": "meal-5", "name": "sweet potatoes", "calories": 230, "price": 3},
    {"id": "meal-6", "name": "salad", "calories": 15, "price": 4},
    {"id": "meal-7", "name": "iced tea", "calories": 70, "price": 2},
    {"id": "meal-8", "name": "lemonade", "calories": 90, "price": 2},
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
    },
]


def calculate_meal_calories(meal_id):
    try:
        meal = next(item for item in meals if item["id"] == meal_id)
        return meal["name"], meal["calories"]
    except StopIteration:
        return f'Meal "{meal_id}" not found'


def calculate_combo_calories(combo_id):
    try:
        combo = next(item for item in combos if item["id"] == combo_id)
        total_calories = sum(
            calculate_meal_calories(meal_id)[1] for meal_id in combo["meals"]
        )
        return combo["name"], total_calories
    except StopIteration:
        return f'Combo "{combo_id}" not found'


# Examples: Calculate calories for meals and combos you need to enter the id of meal n combo
meal_id_1 = "meal-1"
meal_name_1, total_calories_meal_1 = calculate_meal_calories(meal_id_1)
print(f"{meal_name_1} (ID: {meal_id_1}) - Total Calories: {total_calories_meal_1} kcal")

combo_id_1 = "combo-1"
combo_name_1, total_calories_combo_1 = calculate_combo_calories(combo_id_1)
print(
    f"{combo_name_1} (ID: {combo_id_1}) - Total Calories: {total_calories_combo_1} kcal"
)

combo_id_4 = "combo-4"
result = calculate_combo_calories(combo_id_4)
print(result)
