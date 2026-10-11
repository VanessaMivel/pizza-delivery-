# Team 3 pizza delivery app project
# v1 : core structure and basic functionality
#Lead Programmer: Vanessa Swaby

#This program allows users to order pizza from a menu
print("Welcome to Team 3's Pizza Delivery App!")

orders = []
grandTotal = 0.00
anotherOrder = "Y"

while anotherOrder == "Y":

    print("Pizza Sizes")
    print("Small: $15")
    print("Medium: $20")
    print("Large: $25")

    pizzaSize = input("Please select a pizza size (S, M, L): ")
    pizzaSize = pizzaSize.strip().upper()

    while pizzaSize not in ["S", "M","L"]:
        print("Invalid size. Please enter S,M, or L.")
        pizzaSize = input("Please select a pizza size (S, M, L): ")
        pizzaSize = pizzaSize.strip().upper()

    if pizzaSize == "S":
        pizzaPrice = 15
        sizeName = "Small"
    elif pizzaSize == "M":
        pizzaPrice = 20
        sizeName = "Medium"
    else:
        pizzaPrice = 25
        sizeName = "Large"

#Pizza sauces no extra charge 
    print ('\n Choose your sauce:')
    print ('Tomato')
    print ('Alfredo')
    print ('BBQ')
    sauce = input("Please select a sauce (type the name): ").strip().upper()

    while sauce not in ["TOMATO", "ALFREDO", "BBQ"]:
        print("Invalid sauce. Please choose Tomato, Alfredo, or BBQ.")
        sauce = input("Please select a sauce (type the name): ").strip().upper()
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
    meat = input("Please select a meat toppings (type the name): ").strip().upper().split(".")

    for i in range(len(meat)):
        meat[i] = meat[i].strip()

    while (any(topping not in meats for topping in meat) or ("NO MEAT" in meat and len(meat) >1)):
        print("Invalid meat selection. Please try again.")
        meat = input("Please select meat topping(s): ").strip.upper().split(",")

        for i in range(len(meat)):
            meat[i] = meat[i].strip()
        
    meat = list(dict.fromkeys(meat))

    for topping in meat:
        if topping in ["PEPPERONI", "SAUSAGE", "BACON","HAM","CHICKEN"]:
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
    veggie = input("Please select a veggie topping(s),: ")
    veggie = veggie.upper().split(',')

    for i in range(len(veggie)):
        veggie[i] = veggie[i].strip()

    while (any(topping not in veggies for topping in veggie)or ("NO VEGGIES" in veggie and len(veggie) > 1)):
        print("Invalid veggie selection. Please try again.")
        veggie = input("Please select veggie topping(s): ").upper().split(",")

        for i in range(len(veggie)):
            veggie[i] = veggie[i].strip()

    veggie = list(dict.fromkeys(veggie))

    for topping in veggie:
        if topping in ["MUSHROOMS", "ONIONS", "GREEN PEPPERS", "SPINACH", "OLIVES"]:
            if pizzaSize == "S":
                pizzaPrice += 1
            else:
                pizzaPrice += 2

# any sizes are $1 for extra cheese

    print("Cheese Topping")
    cheese = input("Would you like to add extra cheese? (Y/N): ").strip().upper()

    while cheese not in ["Y", "N"]:
        print("Please enter Y or N.")
        cheese = input("Would you like extra cheese? (Y/N): ").strip().upper()

    if cheese == "Y":
        pizzaPrice += 1

#Display order summary
    print("----- ORDER SUMMARY -----")
    print("Size:", sizeName)
    print("Sauce:", sauce.title())
    print("Meat:",",".join(meat).title())
    print("Veggies:",",".join(veggie).title())
    print("Extra cheese:", cheese)
    print(f"Pizza total: ${pizzaPrice:.2f}")

#Confirm the order
    confirmation = input("Would you like to confirm this order? (Y/N): ").strip().upper()

    while confirmation not in ["Y", "N"]:
        print("Please enter Y or N.")
        confirmation = input("Would you like to confirm this order? (Y/N): ").strip().upper()

    if confirmation == "Y":
        orders.append(pizzaPrice)
        grandTotal += pizzaPrice
        print("Your pizza order has been confirmed!")
    else:
        print("Your pizza order has been canceled.")

#Ask about another pizza
    anotherOrder = input("Would you like to order another pizza? (Y/N): ").strip().upper()

    while anotherOrder not in ["Y", "N"]:
        print("Please enter Y or N.")
        anotherOrder = input("Would you like to order another pizza? (Y/N): ").strip().upper()

#Final receipt
print("----- FINAL RECEIPT -----")

for i in range(len(orders)):
      print(f"Pizza {i + 1}: ${orders[i]:.2f}")

print(f"Number of confirmed pizzas: {len(orders)}")
print(f"Final bill: ${grandTotal:.2f}")
print("Thank you for ordering!")
