# Define the calories dictionary
calories = {
    "Hamburger": 600,
    "Cheese Burger": 750,
    "Veggie Burger": 400,
    "Vegan Burger": 350,
    "Sweet Potatoes": 230,
    "Salad": 15,
    "Iced Tea": 70,
    "Lemonade": 90,
    "Pizza Slice (Cheese)": 285,
    "Pizza Slice (Pepperoni)": 311,
    "Grilled Chicken Breast": 165,
    "Fried Chicken Thigh (with skin)": 290,
    "Salmon Fillet (baked)": 206,
    "Pasta (1 cup, cooked)": 200,
    "Rice (1 cup, cooked)": 218,
    "Broccoli (1 cup, steamed)": 55,
    "Avocado": 234,
    "Egg (large, boiled)": 68,
    "Banana": 105,
    "Apple": 95,
    "Greek Yogurt (1 cup)": 100,
    "Almonds (1/4 cup)": 207,
    "Oatmeal (1 cup, cooked)": 166,
}

combos = {
    "Cheesy Combo": ["Cheese Burger", "Sweet Potatoes", "Lemonade"],
    "Veggie Combo": ["Veggie Burger", "Sweet Potatoes", "Iced Tea"],
    "Vegan Combo": ["Vegan Burger", "Salad", "Lemonade"],
    "Chicken Combo": [
        "Grilled Chicken Breast",
        "Broccoli (1 cup, steamed)",
        "Iced Tea",
    ],
    "Salmon Combo": ["Salmon Fillet (baked)", "Salad", "Lemonade"],
}


def calculate_combo_calories(combo_name):
    combo_meals = combos.get(combo_name, [])
    if not combo_meals:
        return f'Combo "{combo_name}" not found'
    total_calories = sum(calories.get(meal, 0) for meal in combo_meals)
    return total_calories


# Examples: Calculate calories for combos
combo_name_1 = "Cheesy Combo"
total_calories_combo_1 = calculate_combo_calories(combo_name_1)
print(f"Total Calories for {combo_name_1}: {total_calories_combo_1} kcal")

combo_name_2 = "Veggie Combo"
total_calories_combo_2 = calculate_combo_calories(combo_name_2)
print(f"Total Calories for {combo_name_2}: {total_calories_combo_2} kcal")

combo_name_3 = "Non-existent Combo"
result = calculate_combo_calories(combo_name_3)
print(result)
