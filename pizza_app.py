# Team 3 pizza delivery app project
# v1 : core structure and basic functionality
#Lead Programmer: Yimian Perez

#This program allows users to order pizza from a menu
print("Welcome to Team 3's Pizza Delivery App!")
print("Pizza Sizes")
print("Small: $15")
print("Medium: $20")
print("Large: $25")

pizzaSize = input("Please select a pizza size (S, M, L): ")
pizzaSize = pizzaSize.upper()

if pizzaSize == "S":
    pizzaPrice = 15
if pizzaSize == "M":
    pizzaPrice = 20
if pizzaSize == "L":
    pizzaPrice = 25

#For pepperoni $2 on S, and $3 on M, and L

print("Pepperoni Topping")
pepperoni = input("Would you like to add pepperoni? (Y/N): ")
pepperoni = pepperoni.upper()

if pepperoni == "Y":
    if pizzaSize == "S":
        pizzaPrice += 2
    else:
        pizzaPrice += 3

# any sizes are $1 for extra cheese

print("Cheese Topping")
cheese = input("Would you like to add extra cheese? (Y/N): ")
cheese = cheese.upper()

if cheese == "Y":
    pizzaPrice += 1

# until clarified by th professor this is the mvp
print(f"Your total cost is: ${pizzaPrice:.2f}")
