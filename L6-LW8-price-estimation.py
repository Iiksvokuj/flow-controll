price = int(input('how much does it cost ? '))

# x ------- 10 ----- 50 ------>
if price <= 10:
    print("Cheap! :)")
elif price <= 50:
    print("Ok! :|")
else:
    print("Expensive! :(")