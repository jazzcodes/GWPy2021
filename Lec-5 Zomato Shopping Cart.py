"""
This file contains information regarding Controller (Zomato use case)
author: Jasleen Kaur
email: jasleenbhambra@gmail.com
Date: July 21, 2021
"""

menu = {
    "Burger": {
        "name": "Veg Burger",
        "price": 100,
        "delivery_time": 10
    },
    "Dal": {
        "name": "Dal Makhani",
        "price": 200,
        "delivery_time": 15
},
    "Paneer": {
        "name": "Shaahi Paneer",
        "price": 300,
        "delivery_time": 20
    }
}

"""
This is can be used but it prints menu after input but we need to show menu before input
dish = input("Enter dish to be purchased: ")
dish_info = menu[dish]
# display menu

print("*"*30)
doubt!!
print("{}         {}".format(dish_info["name"], dish_info["price"]))
print("*"*30)
print()
"""

keys = list(menu.keys())

for keys in menu:
    print("*" * 30)
    print("{}           {}".format(menu[keys]["name"], menu[keys]["price"]))
    print("*" * 30)
    print()

# shopping cart
# empty list
shopping_cart = []


total = 0
while True:
    item = input("Add to Cart (Write 'no' to quit) :")
    if item == "no":
        break

    if item in menu:
        total += menu[keys]["price"]
       # shopping_cart.append(item)
        shopping_cart.append(menu[item])
    else:
        print("Sorry, we don't have",item,"at the moment")

print("Shopping Cart [{}]".format(len(shopping_cart)))
print("Please Pay \u20b9 ", total)
print(shopping_cart)