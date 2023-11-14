# DRAW this PATTERN:
#   * * # * * # * * # * * ...

# HW2: * * * # # * * * # # * * * # # ...

print ("\n")

for x in range(1,21):
    if x % 3 == 0:
        print("# ", end="")
    else:
        print( "* ", end="")

print ("\n")