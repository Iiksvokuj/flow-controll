price = int(input('how much does it cost ? '))

# x ------- 10 ----- 50 ------>
if price <= 10:
    print("Cheap! :)")

if 10 < price <= 50:
    print("Ok! :|")

if price > 50:
    print("Expensive! :(")