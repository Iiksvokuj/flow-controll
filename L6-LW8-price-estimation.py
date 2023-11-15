price = int(input('how much does it cost ? '))

if price < 0:
    print("Price cannot be less then ZERO!!!")
#    quit() # exit this script

# x ------- 10 ----- 50 ------>
elif price <= 10:
    print("Cheap! :)")
elif price <= 50:
    print("Ok! :|")
else:
    print("Expensive! :(")