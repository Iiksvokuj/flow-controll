
# 2. order completion (order flow) ?  (yes/no - True/False)
#     - select food
#     - confirm order (online)
#     - enterclient info
#     - delivery info
#     - payment
#     - delivery (physical)
#     - client satisfied

select_food = False

food_1_name = "Pizza"
food_1_price = 75.00


print ("do you want", food_1_name, "(yes/no)?")
food_1_confirm = input()


if food_1_confirm == 'yes': 

    food_1_quantity = int(input(" - how many? "))
    food_1_cost     = food_1_price * food_1_quantity
    print (food_1_name, "x", food_1_quantity, " = ", food_1_cost )

    select_food = True

    confirm_order = input("confirm (yes/no)? ")
    if confirm_order == 'yes':
        pass
        # HW2:
        #     embed here delivery logic