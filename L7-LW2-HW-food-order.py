# restaurant food order
FOOD_1_NAME   = "Pizza"
FOOD_1_PRICE  = 75.00

FOOD_2_NAME   = "Salad"
FOOD_2_PRICE  = 15.50

DELIVEY_PRICE = 100.00

##########################
# Show menu
print("############# MENU #############")
print("1",FOOD_1_NAME, " : ", FOOD_1_PRICE)
print("2",FOOD_2_NAME, " : ", FOOD_2_PRICE)
print("################################")
#HW1: add code -> "1"
#HW2*: add code, cost > 500, delivery == "y" --> "FREE"
option = input("choose >>> ") #1 -> '1'

if option == "1":   # if Pizza was chosen
    print("you've chosen", FOOD_1_NAME)
    quantity = int(input("How many do you want? "))
    cost = quantity * FOOD_1_PRICE
    print("cost:",cost)
    delivery = input("do you want delivery (y/n)? ")
    if cost >= 500.00:
        DELIVEY_PRICE = 0.00
    if delivery == "y":
        cost = cost + DELIVEY_PRICE
        print("Total with delivery: ", cost)
        if DELIVEY_PRICE == 0:
            print("Delivery is Free!!!")
    elif delivery == "n":
        print("Total cost: ", cost)
if option == "2":   # if Salad was chosen
    print("you've chosen", FOOD_2_NAME)
    quantity = int(input("How many do you want? "))
    cost = quantity * FOOD_2_PRICE
    print("cost: ", cost)
    delivery = input("would you like delivery (y/n)? ")
    if delivery == "y":
        cost = cost + DELIVEY_PRICE
        print("Total with delivery: ", cost)
    elif delivery == "n":
        print ("Total cost: ", cost)
##############################