from os import system
# a - move left
# d - move right

length = 20
roboX = 5
bombX = 15

while True:
    system("cls")

    if roboX == bombX:
        print("❌❌❌ GAME OVER :( ❌❌❌")
        break

    # ########## DRAWING THE MAP ##########
    x = 1
    print("\n")
    while x <= length:
        # HW2: optimize from here
        if x == roboX:
            print("🤖", end = "")
        elif x == bombX:
            print("💣", end = "")
        else:
            print("-", end = "")
        # to here
        x += 1

    print("\n")
    # #####################################

    # ########## CONTROL ##################
    direction = input("dir (a/d/x) > ")
    if direction == 'a':
        roboX -= 1
    if direction == 'd':
        roboX += 1
    if direction == 'x':
        system("cls")
        print("Thank you for playing!!!")
        break
    # ####################################

