# using loops to test algorithms


# X---------v---...---v---...---v--->
# 0         1         10       100


####### Testing case
distance_km = -1
while distance_km <= 101:

    ####### ALGO ##########
    # distance_km = float(input('Enter distance (km): '))
    print("The distance", distance_km,"km\nis:")
    if distance_km <= 1:
        print(" - near")
    elif distance_km <= 10:
        print(" - close")
    elif distance_km <= 100:
        print(" - far")
    else:
        print(" - very far")
    ####### ALGO ##########
    
    distance_km += 1
####### Testing case