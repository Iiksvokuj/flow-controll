
# 1. free delivery? (yes/no - True/False)
#     - client wants delivery ?
#     - vip ?
#     - cost >= 500.00 ?

# delivery_free_limit = 500.00
# delivery_cost       = 100.00
# delivery_wanted_str = input('do you want delivery (yes/no) ? ')
# client_is_vip       = False
# order_cost          = 600.00

#############

# delivery_free_condition_wants = delivery_wanted_str == 'yes'
# delivery_free_condition_vip   = client_is_vip
# delivery_free_condition_cost  = order_cost >= delivery_free_limit

# 2. order completion (order flow) ?  (yes/no - True/False)
#     - select food
#     - confirm order (online)
#     - enterclient info
#     - delivery info
#     - payment
#     - delivery (physical)
#     - client satisfied

## Programm Start

select_food = False

food_1_name = "Pizza"
food_1_price = 75.00
#####
delivery_free_limit = 500.00
delivery_cost       = 100.00
client_is_vip       = False
order_cost          = 600.00
#####

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
        delivery_wanted_str = input('do you want delivery (yes/no) ? ')
        delivery_free_condition_wants = delivery_wanted_str == 'yes'
        delivery_free_condition_vip   = client_is_vip
        delivery_free_condition_cost  = food_1_cost >= delivery_free_limit
        delivery_is_free    = delivery_free_condition_wants\
                              and\
                             (delivery_free_condition_vip or delivery_free_condition_cost)
        delivery_is_free and print ("You've got free delivery.", delivery_is_free)
        not delivery_is_free and print ("You've got to pay", delivery_cost, "for delivery.")



