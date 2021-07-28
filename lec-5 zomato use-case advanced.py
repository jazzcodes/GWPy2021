"""
This file contains information regarding Controller (Zomato use case)
author: Jasleen Kaur
email: jasleenbhambra@gmail.com
Date: July 21, 2021
"""

promo_codes = {
    "NOCOOKING": {
        "min": 169,
        "percentage_discount": 0.20,
        "upto": 100
    },
    "WELCOMEPTM": {
        "min": 299,
        "flat_discount": 75
    }
}

amount = int(input("Enter Amount: "))
print("Available Promo Codes: ")
for promo_code in promo_codes:
    print(promo_code)
promo_code = input("Enter Promo Code: ")
print("Amount: ", amount)
print("Promo Code: ", promo_code)
promo_code_info = promo_codes[promo_code]
if promo_code in promo_codes:
    print("Promo Code is valid!")
    if "percentage_discount" in promo_codes[promo_code]:
        print("We will offer a percentage discount")
        if amount >= promo_code_info["min"]:
            discount = amount * promo_code_info["percentage_discount"]
            if discount <= promo_code_info["upto"]:
                amount -= discount
            else:
                amount -= promo_code_info["upto"]
        else:
            print("Amount is lesser. Please purchase items worth \u20b9", promo_code_info["min"] - amount, " more ")
    else:
        print("We will offer a flat discount")
        if amount >= promo_code_info["min"]:
            amount -= promo_code_info["flat_discount"]
        else:
            print("Amount is lesser. Please purchase items worth \u20b9", promo_code_info["min"] - amount, " more ")

else:
    print("Promo Code is invalid!")

print("Please pay \u20b9", amount)