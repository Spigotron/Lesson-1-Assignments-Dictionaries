restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 17.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99},
}

restaurant_menu["Beverages"] = "Chocolate Milk", "Cream Soda"
main_course = restaurant_menu["Main Course"]
main_course["Steak"] = "15.99"
starters_course = restaurant_menu["Starters"]
starters_course.pop("Bruschetta")

print(restaurant_menu)