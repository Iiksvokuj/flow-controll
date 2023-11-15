# Online Food Order


# 1. free delivery? (yes/no - True/False)
#     - client wants delivery ?
#     - vip ?
#     - cost >= 500.00 ?

delivery_free_limit = 500.00

delivery_wanted_str = input('do you want delivery (yes/no) ? ')
client_is_vip       = False
order_cost          = 600.00

##############
delivery_free_condition_wants = delivery_wanted_str == 'yes'
delivery_free_condition_vip   = client_is_vip
delivery_free_condition_cost  = order_cost >= delivery_free_limit

delivery_is_free    = delivery_free_condition_wants and (delivery_free_condition_vip or delivery_free_condition_cost)
#                                   False                           False                         True
print ("You've got free delivery.", delivery_is_free)

# 2. order completion (order flow) ?  (yes/no - True/False)
#     - select food
#     - confirm order (online)
#     - enterclient info
#     - delivery info
#     - payment
#     - delivery (physical)
#     - client satisfied

