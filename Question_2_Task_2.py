products = {
    "1": {"name": "coaster", "category": "home decor", "price": "20"},
    "2": {"name": "speakers", "category": "electronics", "price": "100"},
    "3": {"name": "pillow", "category": "furniture", "price": "50"}
}

def search():
    search_term = input("Enter the name of the product you'd like to search for. ").lower()
    for key, value in products.items():
        if value["name"].lower() == search_term:
            print(f"Product: {value["name"]}, Category: {value["category"]}, Price: {value["price"]}")
            break
    else:
        print("Sorry, that product is not in our catalog.")

search()