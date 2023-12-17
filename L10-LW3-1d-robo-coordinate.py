# a - move left
# d - move right

length = 20
roboX = 5

while True:
    # ########## DRAWING THE MAP ##########
    x = 1
    print("\n")
    while x <= length:
        # HW2: optimize from here
        if x == roboX:
            print("R", end = "")    #\n
        else:
            print("-", end = "")    #\n
        # to here
        x += 1

    print("\n")
    # #####################################

    # ########## CONTROL ##########
    direction = input("dir (a/d) > ")
    if direction == 'a':
        roboX -= 1
    if direction == 'd':
        roboX += 1
