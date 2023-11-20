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
option = input("choose >>> ") #1 -> '1'

if option == "1":   # if Pizza was chosen
    print("you've chosen", FOOD_1_NAME)
    quantity = int(input("How many o you want? "))
    cost = quantity * FOOD_1_PRICE
    print("cost:",cost)
    delivery = input("do you want delivery (y/n)? ")
    if delivery == "y":
        cost = cost + DELIVEY_PRICE
        print("Total with delivery: ", cost)


