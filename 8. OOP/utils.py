from exception import ItemNotFoundException, InfoNotAvailableException

def calculate_meal_calories(meals, meal_id):
    meal = next((item for item in meals if item["id"] == meal_id), None)
    if meal is not None:
        return meal["name"], meal["calories"]
    else:
        print(f'Meal "{meal_id}" not found')
        return None, None  # Return None values

def calculate_combo_calories(meals, combos, combo_id):
    combo = next((item for item in combos if item["id"] == combo_id), None)
    if combo is not None:
        total_calories = sum(next((meal["calories"] for meal in meals if meal["id"] == meal_id), 0) for meal_id in combo["meals"])
        return combo["name"], total_calories
    else:
        print(f'Combo "{combo_id}" not found')
        return None, None  # Return None values

def calculate_price(meals, combos, item_ids):
    total_price = 0
    total_calories = 0

    meals_data = meals["meals"]
    combos_data = combos["combos"]

    if isinstance(item_ids, list):
        for item_id in item_ids:
            item = next((item for item in meals_data + combos_data if item["id"] == item_id), None)
            if item is not None:
                total_price += item["price"]
                if "calories" in item:
                    total_calories += item["calories"]
                elif "meals" in item:
                    total_calories += sum(calculate_meal_calories(meals_data, meal_id)[1] for meal_id in item["meals"])
            else:
                print(f'Item "{item_id}" not found')  # Print statement instead of raising an exception
                # Continue with the loop or take appropriate action

    else:
        item = next((item for item in meals_data + combos_data if item["id"] == item_ids), None)
        if item is not None:
            total_price = item["price"]
            if "calories" in item:
                total_calories = item["calories"]
            elif "meals" in item:
                total_calories = sum(calculate_meal_calories(meals_data, meal_id)[1] for meal_id in item["meals"])
        else:
            print(f'Item "{item_ids}" not found')  # Print statement instead of raising an exception
            # Take appropriate action

    return total_price, total_calories