# DRAW this PATTERN:
#   * * # * * # * * # * * ...

# HW2: * * * # # * * * # # * * * # # ...

print ("\n")
for n in range(1,5):   
    for x in range(1,6):
        if x % 4 == 0 or x % 5 == 0:
            print("# ", end="")
        else:
            print( "* ", end="")

print ("\n")