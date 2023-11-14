from utils import calculate_price
from datetime import datetime


class Order:
    def __init__(self):
        self._items = []
        self._datetime = datetime.now()

    @property
    def items(self):
        return self._items

    @property
    def datetime(self):
        return self._datetime

    def add_item(self, item_id):
        self._items.append(item_id)

    def calculate_total(self, meals, combos):
        total_price = 0
        total_calories = 0
        for item_id in self._items:
            item = next(
                (item for item in meals + combos if item["id"] == item_id), None
            )
            if item is not None:
                total_price += item["price"]
                if "calories" in item:
                    total_calories += item["calories"]
                elif "meals" in item:
                    for meal_id in item["meals"]:
                        meal = next(
                            (meal for meal in meals if meal["id"] == meal_id), None
                        )
                        if meal is not None and "calories" in meal:
                            total_calories += meal["calories"]
            else:
                print("\033[1;97;35m" + f'-- Item "{item_id}" not found --' + "\033[0m")
        return total_price, total_calories

    def is_order_valid(self, meals, combos):
        total_calories = 0
        unknown_items = []

        items_summary = {}

        for item_id in self._items:
            item = next(
                (item for item in meals + combos if item["id"] == item_id), None
            )
            if item is not None:
                item_name = item["name"]
                item_calories = item.get("calories", 0)

                # If the item is a combo, calculate and add the total calories of its meals
                if "meals" in item:
                    combo_calories = sum(
                        meal["calories"]
                        for meal_id in item["meals"]
                        if "calories"
                        in (
                            meal := next(
                                (meal for meal in meals if meal["id"] == meal_id), None
                            )
                        )
                    )
                    item_calories += combo_calories

                total_calories += item_calories

                if item_name in items_summary:
                    items_summary[item_name]["quantity"] += 1
                    items_summary[item_name]["calories"] += item_calories
                else:
                    items_summary[item_name] = {
                        "quantity": 1,
                        "calories": item_calories,
                    }
            else:
                unknown_items.append(item_id)

        if unknown_items:
            print(
                "\033[1;97;35m"
                + f'-- Order refused: Unknown Items Ordered - {", ".join(unknown_items)} '
                + "\033[0m"
            )
            return False

        if total_calories >= 2000:
            print(
                "\033[1;97;35m"
                + f"-- Order Refused: Total Calories Exceeds 2000 kcal "
                + "\033[0m"
            )
            return False

        return True

    def print_receipt(self, meals, combos):
        if not self.is_order_valid(meals, combos):
            return
        print(f"{'-'*30}\n{'Receipt':^30}\n{'-'*30}")
        total_price, total_calories = self.calculate_total(meals, combos)
        items_summary = {}  # Keep track of item quantities, price, and calories
        for item_id in self._items:
            item = next(
                (item for item in meals + combos if item["id"] == item_id), None
            )
            if item is not None:
                item_name = item["name"]
                item_price = item["price"]
                item_calories = item.get("calories", 0)
                total_price += item_price
                total_calories += item_calories
                if item_name in items_summary:
                    items_summary[item_name]["quantity"] += 1
                    items_summary[item_name]["price"] += item_price
                    items_summary[item_name]["calories"] += item_calories
                else:
                    items_summary[item_name] = {
                        "quantity": 1,
                        "price": item_price,
                        "calories": item_calories,
                    }
                # If the item is a combo, add its meal calories to the combo's calories
                if "meals" in item:
                    for meal_id in item["meals"]:
                        meal = next(
                            (meal for meal in meals if meal["id"] == meal_id), None
                        )
                        if meal is not None and "calories" in meal:
                            item_calories += meal["calories"]
                            items_summary[item_name]["calories"] += meal["calories"]
            else:
                print("\033[1;97;35m" + f'-- Item "{item_id}" not found --' + "\033[0m")
        for item_name, details in items_summary.items():
            print(
                "\033[1;97;40m"
                + f"  {item_name:^20} x{details['quantity']:^8}"
                + "\033[0m"
            )
            print(f"Price: ${details['price']}, Calories: {details['calories']} kcal")
        formatted_datetime = self._datetime.strftime("%Y-%m-%d %H:%M:%S")
        print(
            f'{"-"*35}\n{"Total Price:":<15} ${total_price:>3}\n{"Total Calories:":<3} {total_calories} kcal\n{"Date / Time:":<15} {formatted_datetime}\n{"-"*35}'
        )
