"""
This file contains information regarding Controller -> Logical Statements (if/else, switch case) .
author: Jasleen Kaur
email: jasleenbhambra@gmail.com
Date: July 21, 2021
"""
# if/else
# use case of Zomato

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

amount = input("Enter Amount: ")
promo_code = input("Enter Promo Code: ")
print("Amount: ", amount)
print("Promo Code: ", promo_code)
promo_code_info = promo_codes[promo_code]
if (promo_code in promo_codes) & (int(amount) >= promo_code_info["min"]):
    print("Promo Code is valid!")
    if "percentage_discount" in promo_codes[promo_code]:
        print("We will offer", promo_code_info["percentage_discount"], "% discount")
    else:
        print("We will offer", promo_code_info["flat_discount"], "discount")
else:
    if promo_code not in promo_codes:
        print("Promo Code is invalid!")
    else:
        print("Promo Code is invalid!\nKindly check Terms and Conditions")
