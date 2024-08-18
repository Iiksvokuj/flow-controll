# horisontal path / length
# x1 --------------R-----------------------> x2
# 0                                         n
# roboX - robot coordinate

# HW1: input lenght/roboX
#      check limits

length = int(input("Enter the lenght of traectory [1 - 20]: ")) #20
roboX = int(input("Enter robot coordinates [1 - 20]: "))        # 5
if 1 <= (roboX and length) <= 20 :
    x = 1
    print("\n")
    while x <= length:
        # HW2: optimize from here
        print("-", end = "")
        if x == roboX:
            print("R", end = "")    #\n
        # else:
        #    print("-", end = "")    #\n
        # to here
        x += 1
    print("\n")
else:
    print("\nIncorrect Coordinates!\n")