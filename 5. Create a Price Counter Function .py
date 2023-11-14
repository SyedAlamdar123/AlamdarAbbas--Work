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
    meal = next((item for item in meals if item["id"] == meal_id), None)
    if meal:
        return meal["name"], meal["calories"]
    else:
        return f'Meal "{meal_id}" not found', None


def calculate_combo_calories(combo_id):
    combo = next((item for item in combos if item["id"] == combo_id), None)
    if combo:
        total_calories = sum(
            calculate_meal_calories(meal_id)[1] for meal_id in combo["meals"]
        )
        return combo["name"], total_calories
    else:
        return f'Combo "{combo_id}" not found', None


def calculate_price(item_ids):
    total_price = 0
    total_calories = 0

    if isinstance(item_ids, list):
        for item_id in item_ids:
            item = next(
                (item for item in meals + combos if item["id"] == item_id), None
            )
            if item:
                total_price += item["price"]
                if "calories" in item:
                    total_calories += item["calories"]
                elif "meals" in item:
                    total_calories += sum(
                        calculate_meal_calories(meal_id)[1] for meal_id in item["meals"]
                    )
            else:
                print(f'Item "{item_id}" not found')
                total_price += 0  # Set price to 0 when item is not found
                total_calories += 0  # Set calories to 0 when item is not found
    else:
        item = next((item for item in meals + combos if item["id"] == item_ids), None)
        if item:
            total_price = item["price"]
            if "calories" in item:
                total_calories = item["calories"]
            elif "meals" in item:
                total_calories = sum(
                    calculate_meal_calories(meal_id)[1] for meal_id in item["meals"]
                )
        else:
            print(f'Item "{item_ids}" not found')
            total_price = 0  
            total_calories = 0  # Set price/ calories to 0 when item is not found

    return total_price, total_calories


# Examples: Calculate price for meals
meal_id_1 = "meal-1"
meal_price_1, meal_calories_1 = calculate_price(meal_id_1)
print(f"{meal_id_1} - Price: ${meal_price_1}, Calories: {meal_calories_1} kcal")

# Examples: Calculate price for combo
combo_id_1 = "combo-3"
combo_price_1, combo_calories_1 = calculate_price(combo_id_1)
print(f"{combo_id_1} - Price: ${combo_price_1}, Calories: {combo_calories_1} kcal")

# Examples: Calculate price for items meal | combo meal,meal or combo,meal
combo_ids_2 = ["meal-31", "combo-1"]
combo_price_2, combo_calories_2 = calculate_price(combo_ids_2)
print(f"{combo_ids_2} - Price: ${combo_price_2}, Calories: {combo_calories_2} kcal")

# Example with non-existent item ID
invalid_id = "13"
price, calories = calculate_price(invalid_id)
print(f"{invalid_id} - Price: {price}, Calories: {calories}")
