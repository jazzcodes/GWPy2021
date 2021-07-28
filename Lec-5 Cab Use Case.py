"""
This file contains information regarding Controller (Cab use case)
author: Jasleen Kaur
email: jasleenbhambra@gmail.com
Date: July 21, 2021
"""
# Even more optimal way
cab = input("Please select the cab (bike/mini/sedan): ")
base_fare = 50
cabs = {
    "bike": 20,
    "mini": 50,
    "sedan": 100
}
# kinda exception handling
print("Please pay \u20b9", base_fare + cabs.get(cab, -base_fare))

# there is no switch case in python
# we can use dictionaries to make it

switch = {
    1: "UPI",
    2: "Net Banking",
    3: "Debit Card",
    4: "Credit Card",
    5: "Cash"
}

print(switch)
case = int(input("Choose any one of the above methods to proceed for payment:"))

# doubt!! case is int therefore convert it into int during input , to use in switch.get()
print("You can pay via ", switch.get(case, "Oops! Invalid Choice :/"))

"""
# Optimal Way
cab = input("Please select the cab (bike/mini/sedan): ")
base_fare = 50
cabs = {
    "bike": 20,
    "mini": 50,
    "sedan": 100
}

if cab in cabs:
    print("Please pay \u20b9", base_fare + cabs[cab])
else:
    print("Please book a cab to proceed!")

"""
"""
Traditional Way
# ladder of if-else

base_fare = 50

cab = input("Enter the cab: ")

if cab == "mini":
    fare = base_fare + 50
    print("Please Pay: ", fare)
elif cab == "sedan":
    fare = base_fare + 100
    print("Please Pay: ", fare)
elif cab == "bike":
    fare = base_fare + 20
    print("Please Pay: ", fare)
else:
    print("Please book a cab to proceed!")
"""