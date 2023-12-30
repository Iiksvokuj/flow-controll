# for

# for <variable> in <iterable>:  #str, list, dict, ...
# CODE_TO_REPEAT
# pass / continue


# ####### 1 ... 10

# for n in range(1,11):
#     print(n)

####### HW#1: 1d robo game PRINT MAP -> "for in"  #########

length = int(input("Enter the lenght of traectory [1 - 30]: ")) #30
roboX = int(input("Enter robot coordinates [1 - 30]: "))        # 5
bombX = int(input("Enter bomb coordinates [1 - 30]: "))        # 5

   # ########## DRAWING THE MAP ##########
# x = 1
print("\n")
for x in range(1,length):
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