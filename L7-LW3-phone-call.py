## can we make a call ?

# factor 1
CHARGE_LIMIT  = 2    # %
charge        = 90   # %

# factor 2
BALANCE_LIMIT = -50 # $
balance       = 0   # $

if charge >= CHARGE_LIMIT:
    if balance >= BALANCE_LIMIT:
        print("we can make a call.")
    else:
        print("please pay!")
else:
    print("please charge!")


if balance >= BALANCE_LIMIT:
    print("we can make a call.")
else:
    print("please pay!")