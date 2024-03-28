import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

print(weekly_sales)
copy_of_weekly_sales = copy.deepcopy(weekly_sales)
print(copy_of_weekly_sales)

copy_of_weekly_sales["Week 2"]["Electronics"] = 18000
print(copy_of_weekly_sales)