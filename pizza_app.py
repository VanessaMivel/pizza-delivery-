# Team 3 pizza delivery app project
# v1 : core structure and basic functionality
#Lead Programmer: Vanessa Swaby

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

#Pizza sauces no extra charge 
print ('\n Choose your sauce:')
print ('Tomato')
print ('Alfredo')
print ('BBQ')
sauce = input("Please select a sauce (type the name): ")
sauce = sauce.upper()

#For meats $2 on S, and $3 on M, and L
meats = ["PEPPERONI", "SAUSAGE", "BACON", "HAM", "CHICKEN", "NO MEAT"]
print("Meat Topping")
print ('Choose your meat topping from the following options:')
print ('1.Pepperroni')
print ('2.Sausage')
print ('3.Bacon')
print ('4.Ham')
print ('5.Chicken')
print ('6.No meat')
meat = input("Please select a meat topping (type the name): ")
meat = meat.upper().split(',')

for topping in meat:
    topping = topping.strip()

    if topping in meats:
      if pizzaSize == "S":
        pizzaPrice += 2
      else:
        pizzaPrice += 3


#For veggies $1 on S, and $2 on M, and L
veggies = ["MUSHROOMS", "ONIONS", "GREEN PEPPERS", "SPINACH", "OLIVES", "NO VEGGIES"]
print ("Veggie Topping")
print ('Choose your veggie topping from the following options:')
print ('1.Mushrooms')
print ('2.Onions')
print ('3.Green Peppers')
print ('4.Spinach')
print ('5.Olives')
print ('6.No veggies')
veggie = input("Please select a veggie topping (type the name): ")
veggie = veggie.upper().split(',')

for topping in veggie:
    topping = topping.strip()

    if topping in veggies:
      if pizzaSize == "S":
        pizzaPrice += 1
      else:
        pizzaPrice += 2


# any sizes are $1 for extra cheese

print("Cheese Topping")
cheese = input("Would you like to add extra cheese? (Y/N): ")
cheese = cheese.upper()

if cheese == "Y":
    pizzaPrice += 1

# until clarified by th professor this is the mvp
print(f"Your total cost is: ${pizzaPrice:.2f}")
