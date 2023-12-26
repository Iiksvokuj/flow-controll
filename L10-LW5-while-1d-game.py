# 1d game
# ~~~x~~W~~~

w = 8
x = 2

while True:
    # ######## DRAW MAP ########
    print()

    n = 1
    while n <= 10:
        if n == w:
            print("W", end = " ")
        elif n == x:
            print("x", end = " ")
        else:
            print("~", end = " ")
        n += 1

    print("\n")
    # ######## DRAW MAP ########

    # ####### INTERACTION ######
    direction = input("enter direction(a,d): ")
    # HW1: add limits conditions
    # HW2: add condition mine, "BOOOM!!!" STOP MAIN LOOP
    if direction == "a":
        w -= 1   # w = w - 1
    if direction == "d":
        w += 1   # w = w + 1
    # ####### INTERACTION ######
