# 1d game
# ~~~x~~W~~~

loop = True
w = 8
x = 2

while loop:
    # ######## DRAW MAP ########
    if w == x:
        print("""
              
!!BOOOM!!
 🌪🌪
~ X ~ ~ ~ ~ ~ ~ ~ ~
""")
        loop = False
    else:
        print()
        n = 1
        while n <= 10:
            if n == x:
                print("x", end = " ")
            elif n == w:
                print("W", end = " ")
            else:
                print("~", end = " ")
            n += 1

        print("\n")
        # ######## DRAW MAP ########

        # ####### INTERACTION ######
        direction = input("enter direction(a,d): ")
        # HW1: add limits conditions
        # HW2: add condition mine, "BOOOM!!!" STOP MAIN LOOP
        if direction == "a" and w > 1:
            w -= 1   # w = w - 1
        if direction == "d" and w < 10:
            w += 1   # w = w + 1
        # ####### INTERACTION ######
