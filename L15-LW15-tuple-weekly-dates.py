# app

#     type: list
#       Mo
#       v
week = 20,21,22,23,24,25,26  #or week = (20,21,22,23,24,25,26) -> tuple
week = tuple(week)

print("type of variable type ", type(week))

# modify
# week[6] = 31

###########################################
for day in week:
    print (day)

## tuple       <>      list 
#    ^                   ^
#  read-only          read/write/append/remove/sort/....
#   - for in              - for in
#   - in                  - in
#   - [index]             - [index]      
#     