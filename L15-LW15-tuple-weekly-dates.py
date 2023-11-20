# app

#     type: set
#       Mo
#       v
week            = {20,21,22,23,24,25,26}
# week = set(week)
training_period = {20,22,27,29,4,6}

# get the training days for this week

week_training = week.intersection(training_period)

print("type of variable type ", type(week_training))

###########################################
print("Training for this week:")
for day in week_training:
    print (day)






## tuple       <>      list 
#    ^                   ^
#  read-only          read/write/append/remove/sort/....
#   - for in              - for in
#   - in                  - in
#   - [index]             - [index]      
#     